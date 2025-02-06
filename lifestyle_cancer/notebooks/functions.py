# ========== Proyect Functions ==========

# ---------- libraries ----------
import re
import string
import pandas as pd
from scipy.stats import spearmanr

#  ---------- Function to Calculate the percentage of missing values for each column in a DataFrame ----------
def calculate_missing_values_percentage(df):
    """
    Calculate the percentage of missing values for each column in a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.Series: A Series containing the percentage of missing values for each column.
    """
    missing_values = df.isnull().sum()
    total_rows = df.shape[0]
    missing_values_percentage = (missing_values / total_rows) * 100
    return missing_values_percentage



#  ---------- Function to Converts a column name to snake_case format ----------
def to_snake_case(column_name):
    """
    Converts a column name to snake_case format.

    This function takes a column name as input and returns a new string in snake_case format. 
    Snake case is a naming convention where all letters are lowercase and words are separated by underscores (e.g., 'my_column_name'). 
    It enhances code readability and maintainability, particularly in large projects.

    Args:
        column_name (str): The input column name.

    Returns:
        str: The column name converted to snake_case.
    """
    # Remove punctuation
    column_name = column_name.translate(str.maketrans('', '', string.punctuation)) 

    # Replace spaces with underscores
    column_name = column_name.replace(' ', '_')

    # Insert underscores before uppercase letters (except the first letter)
    column_name = re.sub(r'(?<!^)(?=[A-Z])', '_', column_name)

    # Remove any duplicate underscores
    column_name = re.sub(r'_+', '_', column_name)

    # Convert the entire string to lowercase
    return column_name.lower()




#  ---------- Function to Converts all column names in a DataFrame to snake_case format ----------
def convert_columns_to_snake_case(df):
    """
    Converts all column names in a DataFrame to snake_case format.
    """
    # Applies the to_snake_case function to each column name in the DataFrame
    df.columns = [to_snake_case(col) for col in df.columns]
    return df


#  ---------- Function to create a contengency table ----------
def contingency_table(df, column):
    """
    Create a contingency table between a specified column and the 'probability_of_cancer' column.

    Args:
        df (pd.DataFrame): The input DataFrame.
        column (str): The name of the column to compare with 'probability_of_cancer'.

    Returns:
        pd.DataFrame: A contingency table.
    """
    # Create a contingency table
    table = pd.crosstab(df[column], df['probability_of_cancer'])
    return table


#  ---------- Function to calculate the Spearman correlation between two columns ----------
def calculate_spearman_coefficient(df, column):
    """
    Calculate the Spearman correlation coefficient between a specified column and the 'probability_of_cancer' column.

    Args:
        df (pd.DataFrame): The input DataFrame.
        column (str): The name of the column to compare with 'probability_of_cancer'.

    Returns:
        float: Spearman correlation coefficient.
        float: p-value of the Spearman correlation test.
    """
    # Calcular el coeficiente de Spearman
    spearman_coefficient, p_value = spearmanr(df[column], df['probability_of_cancer'])
    
    return spearman_coefficient, p_value