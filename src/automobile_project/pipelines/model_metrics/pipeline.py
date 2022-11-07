"""
This is a boilerplate pipeline 'model_metrics'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import get_r2_score

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = get_r2_score, 
            inputs = {
                "X_test": "X_test",
                "y_test": "y_test",
                "regressor": "regressor"
                }, 
            outputs = ["y_pred", "regressor_metrics"],
            name = 'get_r2_score'
        )
    ])
