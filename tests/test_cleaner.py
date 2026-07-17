from src.cleaner import clean_column_names
import pandas as pd
import pytest

def test_clean_column_names():
    # Create a sample DataFrame with messy column names
    data = {
        ' Name ': [1, 2, 3],
        'Age': [25, 30, 35],
        ' City ': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    original_columns = df.columns.tolist()
    # Clean the column names
    cleaned_df = clean_column_names(df)
    
    # Expected column names after cleaning
    expected_columns = ['name', 'age', 'city']

    # Assert that the cleaned column names match the expected ones
    assert cleaned_df.columns.tolist() == expected_columns
    assert df.columns.tolist() == original_columns
