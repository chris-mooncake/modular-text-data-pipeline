from pathlib import Path
import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.

    Raises:
        ValueError: If the path is empty or does not point to a CSV file.
        FileNotFoundError: If the file does not exist.
    """
    if not file_path:
        raise ValueError("File path must be a non-empty string.")

    path = Path(file_path)

    if path.suffix.lower() != ".csv":
        raise ValueError("File must have a .csv extension.")

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    return pd.read_csv(path)