def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.

    """
    summary_dataframe = {

        'Feature_name':[col for col in df.columns],
        'Data_type':[df[col].dtype for col in df.columns],
        'Number_of_Unique_Values':[df[col].nunique() for col in df.columns],
        'Missing_Values':[df[col].isnull().any() for col in df.columns]
    }
   
    summary_df = pd.DataFrame(summary_dataframe)

    return summary_df