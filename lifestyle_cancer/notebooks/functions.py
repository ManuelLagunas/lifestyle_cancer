# ========== Proyect Functions ==========

# ---------- libraries ----------
import re

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