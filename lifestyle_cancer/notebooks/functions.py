# ========== Proyect Functions ==========

# ---------- libraries ----------
import re

#  ---------- Function to Converts a column name to snake_case format ----------
def to_snake_case(column_name):
    """
    Converts a column name to snake_case format.
    """
    # Replaces spaces with underscores
    column_name = column_name.replace(' ', '_')
    # Replaces patterns of an uppercase letter following a lowercase letter with an underscore
    column_name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', column_name)
    # Replaces patterns of a lowercase letter or number followed by an uppercase letter with an underscore
    column_name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', column_name)
    # Converts the entire column name to lowercase
    return column_name.lower()


#  ---------- Function to Converts all column names in a DataFrame to snake_case format ----------
def convert_columns_to_snake_case(df):
    """
    Converts all column names in a DataFrame to snake_case format.
    """
    # Applies the to_snake_case function to each column name in the DataFrame
    df.columns = [to_snake_case(col) for col in df.columns]
    return df