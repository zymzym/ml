import pandas as pd
import numpy as np


def get_valid_row_count(data=pd.DataFrame(), threshold: float = 0.5):
    
    """
    This function processes the input DataFrame based on a given threshold and returns an integer result.

    Parameters:
        data (pandas.DataFrame): The input DataFrame to be processed.
        threshold (float): A float value used as a threshold for processing the DataFrame.

    Returns:
        int: An integer result based on the processing of the DataFrame with respect to the threshold.
    """

    if data:
        isnull = data.isnull().sum(axis=1)  # type(isnull_index) = pandas.core.series.Series
        data = data[isnull / data.shape[1] < threshold]
        return data[0]
    else:
        raise ValueError("data is empty")

def get_valid_row(data=pd.DataFrame(), threshold: float = 0.5):
    
    """
    This function processes the input DataFrame based on a given threshold and returns a DataFrame result.

    Parameters:
        data (pandas.DataFrame): The input DataFrame to be processed.
        threshold (float): A float value used as a threshold for processing the DataFrame.

    Returns:
        pandas.DataFrame: A DataFrame result based on the processing of the DataFrame with respect to the threshold.
    """

    if data:
        isnull = data.isnull().sum(axis=1)  # type(isnull_index) = pandas.core.series.Series
        data = data[isnull / data.shape[1] < threshold]
        return data       
    else:
        raise ValueError("data is empty")

def get_valid_column_count(data=pd.DataFrame(), threshold: float = 0.5):

    """
    This function processes the input DataFrame based on a given threshold and returns a interger result.

    Parameters:
        data (pandas.DataFrame): The input DataFrame to be processed.
        threshold (float): A float value used as a threshold for processing the DataFrame.

    Returns:
        int: An integer result based on the processing of the DataFrame with respect to the threshold.
    """

    if data.empty:
        raise ValueError("Data is empty")
    else:
        null_ratio = data.isnull().mean()  # Calculate null ratio for each column
        valid_columns = null_ratio[null_ratio < threshold].index  # Select columns with null ratio below threshold
        return len(valid_columns)
