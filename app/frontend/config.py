import os
# purpose: prepare for deployment, switch environments WITHOUT modifying code.

API_BASE_URL = os.getenv(
    "API_BASE_URL", # Local Development
    "http://127.0.0.1:8000" # Render Deployment
)

PREDICT_ENDPOINT = f"{API_BASE_URL}/predict"