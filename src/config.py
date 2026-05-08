# src/config.py
# Purpose: Central place for constants

TARGET_COL = "ICU"
ID_COL = "PATIENT_VISIT_IDENTIFIER"

CATEGORICAL_COLS = [
    'AGE_PERCENTIL',
    'AGE_ABOVE65',
    'GENDER',
    'DISEASE GROUPING 1',
    'DISEASE GROUPING 2',
    'DISEASE GROUPING 3',
    'DISEASE GROUPING 4',
    'DISEASE GROUPING 5',
    'DISEASE GROUPING 6',
    'HTN',
    'IMMUNOCOMPROMISED',
    'OTHER'
]

DATA_PATH = "data/processed/df_model.csv"

# Logistic Regression hyperparameters
MAX_ITER = 1000

# RandomForest hyperparameters
RANDOM_STATE = 42
N_ESTIMATORS= 100
MAX_DEPTH= None

# XGBoost hyperparameters
EVAL_METRIC = "logloss"

# Test size
TEST_SIZE = 0.2


