from src.cleaner import clean_column_names
from src.cleaner import remove_duplicates
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

def test_remove_duplicates():
    # Create a sample DataFrame with duplicate rows
    data = {
        'Name': ['Alice', 'Bob', 'Alice', 'Charlie'],
        'Age': [25, 30, 25, 35]
    }
    df = pd.DataFrame(data)
    original_length = len(df)
    
    # Remove duplicates
    cleaned_df = remove_duplicates(df)
    
    # Assert that the cleaned DataFrame has fewer rows than the original
    assert len(cleaned_df) == 3
    # Assert that the cleaned DataFrame has no duplicate rows
    assert cleaned_df.duplicated().sum() == 0
    assert len(df) == original_length  # Ensure the original DataFrame is unchanged


