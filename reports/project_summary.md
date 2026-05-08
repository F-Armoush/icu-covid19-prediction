# ICU Prediction for COVID-19 Patients (Early-Stage ML Model)

## Project Summary

This project develops a machine learning pipeline to predict whether a COVID-19 patient will require ICU admission using only early-stage clinical data (0–2 hours).

The objective is to support early risk identification and clinically realistic ICU prediction using leakage-safe patient-level modeling.

---

## Problem Framing

* **Task:** Binary classification (ICU admission)
* **Input:** Early clinical, demographic, and laboratory features
* **Constraint:** Use only the first observation window (0–2 hours)
* **Goal:** Predict future ICU admission (not current ICU state)

To ensure clinical realism and avoid temporal leakage, each patient is represented once using only early-stage information.

---

## Dataset

* 385 confirmed COVID-19 patients
* Multiple temporal observation windows per patient:

  * 0–2 hours
  * 2–4 hours
  * 4–6 hours
  * 6–12 hours
  * Above 12 hours

### Final Modeling Dataset

* One row per patient
* Only the first observation window (0–2 hours) retained
* Patient-level ICU target
* Leakage-safe dataset design

The processed dataset (`df_model.csv`) was generated during preprocessing and used for all training and evaluation experiments.

---

## Methodology

### Data Strategy

* Restricted modeling to the first observation window (0–2 hours)
* Constructed a patient-level ICU target
* Removed post-admission information to prevent temporal leakage

### Preprocessing

* Removed features with >60% missing values
* Numerical features:

  * Median imputation
  * Standard scaling
* Categorical features:

  * Most frequent imputation
  * One-hot encoding

### Modeling

The following models were evaluated:

* Logistic Regression (baseline)
* Random Forest
* XGBoost

All experiments used a stratified 80/20 train-test split.

---

## Results

| Model         | Accuracy   | Precision | Recall     | F1         | ROC-AUC    |
| ------------- | ---------- | --------- | ---------- | ---------- | ---------- |
| logistic      | 0.6883     | 0.6829    | 0.7179     | 0.7000     | 0.6920     |
| random_forest | **0.7013** | 0.6667    | **0.8205** | **0.7356** | 0.7203     |
| xgboost       | 0.6494     | 0.6304    | 0.7436     | 0.6824     | **0.7379** |

---

## Model Selection

Random Forest was selected as the final model based on its overall balance between recall and F1-score, which are particularly important for this clinical use case.

### Selection Rationale

* Highest F1-score across evaluated models
* Highest recall (~0.82), reducing false negatives
* Stable performance across metrics
* Effective handling of non-linear relationships in tabular clinical data

Although XGBoost achieved a slightly higher ROC-AUC, Random Forest provided the most suitable trade-off for early ICU risk prediction.

From a clinical perspective, minimizing false negatives (missed ICU cases) is a priority.

---

## Key Insights

The model identified clinically meaningful predictors associated with ICU admission risk, including:

* Age
* Lymphocyte levels
* Urea
* C-reactive protein (PCR)
* Platelets
* Sodium levels

These findings align with known indicators of COVID-19 severity.

---

## Engineering and Reproducibility

The project was refactored from exploratory notebooks into a modular and reproducible machine learning system.

Implemented engineering improvements include:

* Modular package structure (`src/`)
* Reusable preprocessing pipeline
* CLI execution interface (`run.py`)
* Versioned model persistence
* Metrics tracking using JSON artifacts
* Automated evaluation report generation
* Versioned figure and report saving
* Windows-safe path handling
* Reproducible training workflow

The best-performing model is automatically selected, versioned, and saved during training.

---

## Key Takeaways and Next Steps

* Early-stage ICU prediction is feasible using limited clinical data when temporal structure is handled correctly
* Restricting the dataset to the first observation window (0–2 hours) is essential to prevent temporal leakage
* Tree-based models outperformed linear models on this dataset
* Model behavior aligns with established clinical indicators of COVID-19 severity

Potential future improvements include:

* Hyperparameter optimization
* Cross-validation
* Probability calibration
* Deployment as a clinical decision support tool
