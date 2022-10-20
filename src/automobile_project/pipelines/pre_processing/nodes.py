"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.3
"""
import pandas as pd

def pre_processing(df: pd.DataFrame) -> pd.DataFrame: 
    """This method drop columns 'normalized-losses'
    and drop Nan values (rows)

    Args:
        df (pd.DataFrame): raw df

    Returns:
        pd.DataFrame: pre process df
    """
    df=df.drop(columns=['normalized-losses'])
    
    df.dropna(inplace=True)
    
    return df