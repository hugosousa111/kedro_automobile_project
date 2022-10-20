"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.3
"""
import pandas as pd
from typing import Dict
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def split_train_test(
    df: pd.DataFrame, 
    test_size: float = 0.3, 
    random_state: int = 42
    ) -> Dict[str, pd.DataFrame]:
    """Split data in X (dependent variable) and y (independent variable)
    Split X and y in  X train and test, y train and test
    
    Args:
        df (pd.DataFrame): pre processed df 
        test_size (float, optional): size of df test data. Defaults to 0.3.
        random_state (int, optional): random seed. Defaults to 42.

    Returns:
        Dict[str, pd.DataFrame]: dict of data, train and test
    """
    X = df.drop('price', axis = 1)
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
        )

    return dict(
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
    )

def fit_model(
    X_train: pd.DataFrame, 
    X_test: pd.DataFrame, 
    y_train: pd.DataFrame, 
    y_test: pd.DataFrame) -> LinearRegression:
    regressor = LinearRegression()

    regressor.fit(X_train,y_train)

    y_pred = regressor.predict(X_test)
    
    r2 = r2_score(y_test,y_pred)
    print(f'R2 = {r2}')

    return regressor 