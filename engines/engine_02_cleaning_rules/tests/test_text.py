import pandas as pd
from src.clean_text import clean_text

def test_text_mapping_gender():
    df = pd.DataFrame({
        "gender": ["Male", "pr", "FEMALE"]
    })

    cleaned = clean_text(df)

    assert set(cleaned["gender"].unique()) == {"male", "female"}
