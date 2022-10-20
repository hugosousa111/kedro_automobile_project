"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import pre_processing

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = pre_processing,
            inputs = "raw_dataset",
            outputs = "pp_dataset",
            name = 'pre_processing'
            ),
    ])