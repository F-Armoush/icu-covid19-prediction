# app/utils/inference.py
# Purpose:
# 1. load expected feature schema
# 2. build full prediction dataframe
# 3. safely fill missing columns

import pandas as pd


def build_inference_dataframe(user_input, expected_columns):

    """
    Build a full inference dataframe aligned with
    the training schema expected by the pipeline.
    """

    # -------------------------
    # Start with empty row
    # -------------------------

    data = {}

    # -------------------------
    # Fill all expected columns
    # -------------------------

    for col in expected_columns:

        # Use user-provided value if available
        if col in user_input:

            data[col] = user_input[col]

        # Otherwise fill with None
        else:

            data[col] = None

    # -------------------------
    # Create dataframe
    # -------------------------

    df = pd.DataFrame([data])

    return df