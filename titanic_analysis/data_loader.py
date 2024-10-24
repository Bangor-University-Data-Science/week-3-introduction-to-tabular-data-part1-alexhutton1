import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    """
    Loads the Titanic dataset from the specified file path.
    
    Args:
        filepath (str): Path to the Titanic CSV file.
    
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    """
    #df = pd.read_csv(filepath)
    df = pd.read_csv("https://github.com/Bangor-University-Data-Science/week-3-introduction-to-tabular-data-part1-alexhutton1/blob/main/data/titanic.csv")
    return df
