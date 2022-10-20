"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.3
"""
import pandas as pd
from typing import Dict

from sklearn.preprocessing import OrdinalEncoder

def ordinal_encoder_str_columns(df: pd.DataFrame) -> Dict[pd.DataFrame, OrdinalEncoder]:
    """This method encode all str columns in df
    Str columns: 
        'make', 'fuel-type', 
        'aspiration', 'num-of-doors', 
        'body-style', 'drive-wheels', 
        'engine-location', 'engine-type',
        'num-of-cylinders', 'fuel-system'
        
    Args:
        df (pd.DataFrame): df with str columns

    Returns:
        Dict[pd.DataFrame, OrdinalEncoder]: df encoded and ordinal encoder transformer
    """
    columns_to_transform = [
        'make', 'fuel-type', 
        'aspiration', 'num-of-doors', 
        'body-style', 'drive-wheels', 
        'engine-location', 'engine-type',
        'num-of-cylinders', 'fuel-system'
        ]
    
    oe_transformer = OrdinalEncoder()
    
    df[columns_to_transform] = oe_transformer.fit_transform(df[columns_to_transform])
    
    return df, oe_transformer
