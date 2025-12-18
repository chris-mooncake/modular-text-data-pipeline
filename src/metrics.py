import pandas as pd


def class_counts(input_dataframe: pd.DataFrame, col_name: str) -> pd.Series:
    """
    Returns the count for each unique value in a given column.

    Args:
        input_dataframe (pd.DataFrame): Pandas DataFrame with data.
        col_name (str): Name of the column to with string data.

    Returns:
        pd.Series: Series with name and count for each unique value.
    
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

    return input_dataframe[col_name].value_counts()


def basic_statistical_metrics(input_dataframe: pd.DataFrame, col_name: str) -> dict:
    """
    Return dictionary of mean, median and standard deviation for a given numerical column.

    Args:
        input_dataframe (pd.DataFrame): Pandas DataFrame with data.
        col_name (str): Name of the column to with int or float data.

    Returns:
        pd.DataFrame: Dictionary with keys Mean, Median and Standard deviation.
    
    Raises:
        ValueError: If the input variable is empty or column name not in DataFrame.
        TypeError: If the input variable is not a Pandas DataFrame or the given column doesn't contain int or float data.
    """
    if not isinstance(input_dataframe, pd.DataFrame):
        raise TypeError("Input variable must be a Pandas DataFrame.")

    if input_dataframe.empty:
        raise ValueError("Input DataFrame cannot be empty.")
    
    if col_name not in input_dataframe.columns:
        raise ValueError("Column name not in DataFrame.")
    
    if not pd.api.types.is_numeric_dtype(input_dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' must contain int or float data.")

    output_dictionary = {
        "Mean": input_dataframe[col_name].mean(),
        "Median": input_dataframe[col_name].median(),
        "Standard deviation": input_dataframe[col_name].std()
    }

    return output_dictionary