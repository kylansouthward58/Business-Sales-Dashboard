import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the column names of a DataFrame by removing leading/trailing whitespace,
    converting to lowercase, and replacing spaces with underscores.

    """
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
    return df
    
def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicate rows from a DataFrame.

    """
    df = df.copy()
    df = df.drop_duplicates()
    return df