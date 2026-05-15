# app/api/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import joblib
import pandas as pd
import os

from app.utils.inference import build_inference_dataframe


# --------------------------------------------------
# FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="ICU Prediction API",
    description="Predict ICU admission risk using early-stage clinical data. By Firas Armoush",
    version="1.0"
)


# --------------------------------------------------
# Load trained model
# --------------------------------------------------

BASE_DIR = os.path.dirname(__file__)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "..",
    "..",
    "models"
)

# Load latest Random Forest model
model_files = [
    f for f in os.listdir(MODEL_DIR)
    if f.startswith("random_forest") and f.endswith(".pkl")
]

latest_model = sorted(model_files)[-1]

MODEL_PATH = os.path.join(
    MODEL_DIR,
    latest_model
)

model = joblib.load(MODEL_PATH)

print(f"Loaded model: {latest_model}")


# --------------------------------------------------
# Input schema
# --------------------------------------------------

class PatientData(BaseModel):

    AGE_ABOVE65: Optional[int] = None
    GENDER: Optional[int] = None
    HTN: Optional[int] = None
    IMMUNOCOMPROMISED: Optional[int] = None

    ALBUMIN_MEDIAN: Optional[float] = None
    BE_ARTERIAL_MEDIAN: Optional[float] = None
    PCR_MEDIAN: Optional[float] = None
    UREA_MEDIAN: Optional[float] = None
    CREATININ_MEDIAN: Optional[float] = None

    HEART_RATE_MEDIAN: Optional[float] = None
    RESPIRATORY_RATE_MEDIAN: Optional[float] = None
    OXYGEN_SATURATION_MEDIAN: Optional[float] = None

    TEMPERATURE_MEDIAN: Optional[float] = None


# --------------------------------------------------
# Root endpoint
# --------------------------------------------------

@app.get("/")
def root():

    return {
        "message": "ICU Prediction API is running"
    }


# --------------------------------------------------
# Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict(data: PatientData):

    # ----------------------------------------------
    # Convert request to dictionary
    # ----------------------------------------------

    user_input = data.dict()

    # ----------------------------------------------
    # Get expected training schema
    # ----------------------------------------------

    expected_columns = model.feature_names_in_

    # ----------------------------------------------
    # Build full inference dataframe
    # ----------------------------------------------

    input_df = build_inference_dataframe(
        user_input=user_input,
        expected_columns=expected_columns
    )

    # ----------------------------------------------
    # Generate prediction
    # ----------------------------------------------

    probability = model.predict_proba(input_df)[0][1]

    prediction = int(probability >= 0.5)

    # ----------------------------------------------
    # Return response
    # ----------------------------------------------

    return {

        "icu_probability": round(float(probability), 4),

        "prediction": prediction,

        "risk_level": (
            "High Risk"
            if prediction == 1
            else "Low Risk"
        )
    }