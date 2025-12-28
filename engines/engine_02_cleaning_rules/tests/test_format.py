import pandas as pd
from src.clean_format import validate_dates, validate_numeric

def test_validate_dates_invalid_to_null():
    df = pd.DataFrame({
        "date": ["2020-01-01", "invalid"]
    })

    cleaned = validate_dates(df)

    assert cleaned["date"].isnull().sum() == 1


def test_validate_numeric_symbol_removed():
    df = pd.DataFrame({
        "income": ["5.000", "-"]
    })

    cleaned = validate_numeric(df)

    assert cleaned["income"].isnull().sum() == 1
