"""
This is a boilerplate pipeline 'model_metrics'
generated using Kedro 0.18.3
"""
import pandas as pd
from typing import Dict, Union, List
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def get_r2_score(
    X_test: pd.DataFrame, 
    y_test: pd.DataFrame,
    regressor: LinearRegression
    ) -> Dict[str, Union[float, List[float]]]:

    y_pred = regressor.predict(X_test)
    
    r2 = r2_score(y_test,y_pred)

    y_pred = pd.DataFrame(y_pred, columns = ['price_predict'])
    return y_pred, {"r2_score": {"value": r2, "step": 1}}