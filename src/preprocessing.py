import pandas as pd


def drop_rows_with_missing_values(input_dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Drops rows with missing values.

    Args:
        input_dataframe (pd.DataFrame): Pandas DataFrame with data.

    Returns:
        pd.DataFrame: Cleaned copy of input DataFrame.
    
    Raises:
        ValueError: If the input variable is empty.
        TypeError: If the input variable is not a Pandas DataFrame.
    """
    if not isinstance(input_dataframe, pd.DataFrame):
        raise TypeError("Input variable must be a Pandas DataFrame.")

    if input_dataframe.empty:
        raise ValueError("Input DataFrame cannot be empty.")

    output_dataframe = input_dataframe.dropna()

    return output_dataframe


def column_names_to_snake_case(input_dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Changes column names to snake case.

    Args:
        input_dataframe (pd.DataFrame): Pandas DataFrame with data.

    Returns:
        pd.DataFrame: Copy of input DataFrame with cleaned column names.

    Raises:
        ValueError: If the input variable is empty.
        TypeError: If the input variable is not a Pandas DataFrame.
    """
    if not isinstance(input_dataframe, pd.DataFrame):
        raise TypeError("Input variable must be a Pandas DataFrame.")

    if input_dataframe.empty:
        raise ValueError("Input DataFrame cannot be empty.")

    output_dataframe = input_dataframe.copy()
    output_dataframe.columns = (
    output_dataframe.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )


    return output_dataframe
