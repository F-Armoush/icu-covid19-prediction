# src/plots.py
# Purpose: Generate and save evaluation figures

import os
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay
)


def save_confusion_matrix(y_test, y_pred, save_path):

    ConfusionMatrixDisplay.from_predictions(y_test, y_pred)

    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def save_roc_curve(y_test, y_proba, save_path):

    RocCurveDisplay.from_predictions(y_test, y_proba)

    plt.title("ROC Curve")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def save_feature_importance(best_model, save_path, top_n=20):

    model_step = best_model.named_steps["model"]

    # Check if model supports feature importance
    if not hasattr(model_step, "feature_importances_"):
        return None

    feature_names = (
        best_model
        .named_steps["preprocessor"]
        .get_feature_names_out()
    )

    importances = model_step.feature_importances_

    fi = pd.DataFrame({
        "feature": feature_names,
        "importance": importances
    })

    fi = (
        fi.sort_values("importance", ascending=False)
        .head(top_n)
    )

    plt.figure(figsize=(10, 6))

    plt.barh(
        fi["feature"][::-1],
        fi["importance"][::-1]
    )

    plt.title(f"Top {top_n} Feature Importances")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

    return fi