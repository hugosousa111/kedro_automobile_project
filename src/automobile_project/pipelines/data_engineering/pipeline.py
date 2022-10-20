"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import ordinal_encoder_str_columns

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = ordinal_encoder_str_columns, 
            inputs = "pp_dataset", 
            outputs = ["dataset_expanded", "oe_transformer"],
            name = 'ordinal_encoder_str_columns'
        )
    ])
