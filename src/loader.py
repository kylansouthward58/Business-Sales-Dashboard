import pandas as pd
from pathlib import Path

def load_csv(file_path: str) -> pd.DataFrame:
    """
   Validates the file path and loads a CSV into a DataFrame while providing meaningful errors when loading fails.
    """

    path_file = Path(file_path)

    if not path_file.exists():
        raise FileNotFoundError("The CSV file does not exist.")

    if not path_file.is_file():
        raise ValueError("The provided path is not a file.")

    if path_file.suffix != ".csv":
        raise ValueError("File must be a CSV.")

    try:
        df = pd.read_csv(file_path)
        return df

    except PermissionError:
        raise PermissionError("Permission denied when accessing the file.")

    except pd.errors.EmptyDataError:
        raise ValueError("The CSV file is empty.")