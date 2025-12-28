import pandas as pd
from src.clean_missing import clean_missing

def test_clean_missing_removes_null():
    df = pd.DataFrame({
        "age": [20, None, 30]
    })

    cleaned = clean_missing(df)

    assert cleaned["age"].isnull().sum() == 0
