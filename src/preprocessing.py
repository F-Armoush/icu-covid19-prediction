# src/preprocessing.py
# Purpose: Build pipeline

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from .config import CATEGORICAL_COLS, TARGET_COL, ID_COL

def get_feature_columns(df):
    numeric_cols = [
        col for col in df.columns
        if col not in CATEGORICAL_COLS + [TARGET_COL, ID_COL]
    ]
    return numeric_cols, CATEGORICAL_COLS

def build_preprocessor(numeric_cols, categorical_cols):

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("num", numeric_pipeline, numeric_cols),
        ("cat", categorical_pipeline, categorical_cols)
    ])

    return preprocessor