from src.loader import load_csv
import pandas as pd
import pytest


def test_load_valid_csv():
    file_path = "data/raw/titanic.csv"

    df = load_csv(file_path)
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_missing_file():
    file_path = "data/raw/fake_file.csv"
    with pytest.raises(FileNotFoundError):
        load_csv(file_path)
    
def test_invalid_file_extension():
    with pytest.raises(ValueError):
        load_csv('data/raw/sample_file.txt')

def test_empty_csv():
    with pytest.raises(ValueError):
        load_csv('data/raw/empty.csv')

