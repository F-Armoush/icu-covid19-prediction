# app/frontend/utils.py
# modular frontend architecture

def get_risk_level(probability):

    """
    Convert probability into
    human-readable risk category.
    """

    if probability >= 0.80:
        return "Very High Risk"

    elif probability >= 0.60:
        return "High Risk"

    elif probability >= 0.40:
        return "Moderate Risk"

    else:
        return "Low Risk"


def get_risk_color(probability):

    """
    Streamlit color helper.
    """

    if probability >= 0.80:
        return "red"

    elif probability >= 0.60:
        return "orange"

    elif probability >= 0.40:
        return "yellow"

    return "green"