import pandas as pd
from src.clean_duplicates import remove_duplicates

def test_remove_duplicates():
    df = pd.DataFrame({
        "id": [1, 1, 2],
        "name": ["A", "A", "B"]
    })

    cleaned = remove_duplicates(df)

    assert len(cleaned) == 2
