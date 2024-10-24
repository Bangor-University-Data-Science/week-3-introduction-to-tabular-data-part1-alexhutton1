def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """

    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.to_list()
    categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns.to_list()

    feature_types = {
        'numerical': {
            'continuous': [col for col in numerical_cols if df[col].nunique() > 20 ],  # Fill with continuous numerical features
            'discrete': [col for col in numerical_cols if df[col].nunique() <= 20 ]  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': [col for col in categorical_cols if df[col].nunique() < 5],  # Fill with nominal categorical features
            'ordinal': [col for col in categorical_cols if df[col].nunique() > 5]  # Fill with ordinal categorical features
        }
    }
    return feature_types
