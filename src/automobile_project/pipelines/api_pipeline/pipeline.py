from kedro.pipeline import Pipeline, node

from .nodes import save_predictor


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=save_predictor,
                name="save_predictor",
                inputs={
                    "regressor": "regressor", 
                    "oe_transformer": "oe_transformer"
                },
                outputs="MLPredictor",
            )
        ]
    )