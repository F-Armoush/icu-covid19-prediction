# ICU Prediction for COVID-19 Patients (Early-Stage Machine Learning Model)

## Overview

This project develops a machine learning pipeline to predict whether a patient with confirmed COVID-19 will require Intensive Care Unit (ICU) admission using only early-stage clinical data (first 0–2 hours).

The objective is to enable early risk identification to support clinical decision-making and efficient ICU resource allocation.

---

## Business / Clinical Problem

Early identification of patients at risk of severe deterioration is critical in managing COVID-19 cases.

Accurate ICU prediction can support:

* Prioritized patient monitoring
* Efficient ICU resource allocation
* Timely clinical intervention

This project focuses on clinically realistic early prediction, following the principle:

> “The earlier, the better.”

---

## Dataset

The dataset contains clinical and laboratory measurements for **385 confirmed COVID-19 patients**, each observed across multiple time windows:

* 0–2 hours
* 2–4 hours
* 4–6 hours
* 6–12 hours
* Above 12 hours

### Final Modeling Dataset

To prevent temporal leakage and ensure clinically meaningful prediction:

* Only the first observation window (0–2 hours) is used
* Each patient is represented once
* The target reflects future ICU admission

The processed dataset (`df_model.csv`) is generated during the EDA stage and represents a leakage-safe, patient-level dataset used for model training and evaluation.

---

## Methodology

### Data Strategy

* Restricted analysis to the first observation window (0–2 hours)
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

### Final Dataset

* 385 patients
* 192 engineered input features after preprocessing and encoding

* Note: 
  * df_model.csv shape is (385.194) that 192 features pluse the "target_col" and "id_col".
  
---

## Modeling

The following models were evaluated:

* Logistic Regression (baseline)
* Random Forest
* XGBoost

All models were trained using a stratified 80/20 train-test split.

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

* Highest F1-score across all evaluated models
* Highest recall (~0.82), reducing false negatives
* Stable performance across evaluation metrics


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

The project was refactored from exploratory notebooks into a modular and reproducible machine learning pipeline.

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

## Project Structure

```text
icu-covid19-prediction/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_eda_and_data_understanding.ipynb
│   └── 02_model_experiments.ipynb
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   └── plots.py
├── models/
├── reports/
│   ├── figures/
│   └── evaluation_<timestamp>.md
├── results/
│   └── metrics_<timestamp>.json
├── run.py
├── README.md
└── requirements.txt
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/F-Armoush/icu-covid19-prediction.git
cd icu-covid19-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the training pipeline

```bash
python run.py
```

The pipeline will:

* Train all models
* Evaluate performance
* Select the best model automatically
* Save the trained model
* Save evaluation metrics
* Generate evaluation reports and figures

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
* External validation on additional cohorts
* Deployment as a clinical decision support tool

