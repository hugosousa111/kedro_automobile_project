"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_train_test, fit_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = split_train_test, 
            inputs = {
                "df": "dataset_expanded", 
                "test_size": "params:test_size",
                "random_state": "params:random_state"
                },
            outputs = {
                "X_train": "X_train",
                "y_train": "y_train",
                "X_test": "X_test",
                "y_test": "y_test",
                }, 
            name = 'split_train_test'
        ),
        node(
            func = fit_model, 
            inputs = {
                "X_train": "X_train",
                "y_train": "y_train",
                }, 
            outputs = "regressor",
            name = 'fit_model'
        )
    ])