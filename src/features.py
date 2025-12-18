import pandas as pd


def categorize_column(input_dataframe: pd.DataFrame, col_name: str) -> pd.DataFrame:
    """
    Converts categories in given column to numeric codes. The function uses automatic categorical encoding.
    For missing values it will place -1. Order is arbitrary and codes are dataset-dependent.

    Args:
        input_dataframe (pd.DataFrame): Pandas DataFrame with data.
        col_name (str): Name of the column to transform.

    Returns:
        pd.DataFrame: Copy of original DataFrame with transformed column.
    
    Raises:
        ValueError: If the input variable is empty or column name not in DataFrame.
        TypeError: If the input variable is not a Pandas DataFrame.
    """
    if not isinstance(input_dataframe, pd.DataFrame):
        raise TypeError("Input variable must be a Pandas DataFrame.")

    if input_dataframe.empty:
        raise ValueError("Input DataFrame cannot be empty.")
    
    if col_name not in input_dataframe.columns:
        raise ValueError("Column name not in DataFrame.")

    output_dataframe = input_dataframe.copy()
    output_dataframe[col_name] = output_dataframe[col_name].astype("category").cat.codes

    return output_dataframe


def add_word_count_col(input_dataframe: pd.DataFrame, col_name: str) -> pd.DataFrame:
    """
    Adds new column to the data frame named word_count with the number of words present for each row in input column name.

    Args:
        input_dataframe (pd.DataFrame): Pandas DataFrame with data.
        col_name (str): Name of the column to with string data.

    Returns:
        pd.DataFrame: Copy of original DataFrame with word count column.
    
    Raises:
        ValueError: If the input variable is empty or column name not in DataFrame.
        TypeError: If the input variable is not a Pandas DataFrame or the given column doesn't contain string data.
    """
    if not isinstance(input_dataframe, pd.DataFrame):
        raise TypeError("Input variable must be a Pandas DataFrame.")

    if input_dataframe.empty:
        raise ValueError("Input DataFrame cannot be empty.")
    
    if col_name not in input_dataframe.columns:
        raise ValueError("Column name not in DataFrame.")
    
    if not pd.api.types.is_string_dtype(input_dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' must contain string data.")

    output_dataframe = input_dataframe.copy()
    output_dataframe["word_count"] = output_dataframe[col_name].str.split().str.len()

    return output_dataframe