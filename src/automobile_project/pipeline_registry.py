"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from automobile_project.pipelines import pre_processing as pp
from automobile_project.pipelines import data_engineering as de
from automobile_project.pipelines import data_science as ds

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    
    pre_processing_pipeline = pp.create_pipeline()
    data_engineering_pipeline = de.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
        
    pipelines = {
        "pp": pre_processing_pipeline,
        "de": data_engineering_pipeline,
        "ds": data_science_pipeline,
        "__default__": (
            pre_processing_pipeline
            + data_engineering_pipeline
            + data_science_pipeline
        )
    }
    return pipelines