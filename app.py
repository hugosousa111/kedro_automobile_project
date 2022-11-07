import os
import pandas as pd
from pathlib import Path
from kedro.framework.startup import bootstrap_project
from kedro.framework.session import KedroSession
from enum import Enum
from fastapi import FastAPI, Request, Header, HTTPException, Body
from fastapi.responses import RedirectResponse
from typing import Iterable, Tuple, Optional
from itertools import chain

project_path = Path.cwd()
metadata = bootstrap_project(project_path)
session = KedroSession.create(metadata.package_name, project_path)
context = session.load_context()

app = FastAPI(
    title="FastAPI",
    version="0.1.0",
    description="""
        ChimichangApp API helps you do awesome stuff. 🚀
## Items
You can **read items**.
## Users
You will be able to:
* **Create users** (_not implemented_). * **Read users** (_not implemented_).

    """,
    openapi_tags=[{'name': 'users', 'description': 'Operations with users. The **login** logic is also here.'}, {'name': 'items', 'description': 'Manage items. So _fancy_ they have their own docs.'}]
)

@app.get('/')
async def docs_redirect():
    return RedirectResponse(url='/docs')


MLPredictor = context.catalog.load("MLPredictor")



class MLPredictormake(str, Enum):
    alfa_romero = "alfa_romero"
    audi = "audi"
    bmw = "bmw"
    chevrolet = "chevrolet"
    dodge = "dodge"
    honda = "honda"
    isuzu = "isuzu"
    jaguar = "jaguar"
    mazda = "mazda"
    mercedes_benz = "mercedes_benz"
    mercury = "mercury"
    mitsubishi = "mitsubishi"
    nissan = "nissan"
    peugot = "peugot"
    plymouth = "plymouth"
    porsche = "porsche"
    saab = "saab"
    subaru = "subaru"
    toyota = "toyota"
    volkswagen = "volkswagen"
    volvo = "volvo"
    

class MLPredictorfuel_type(str, Enum):
    gas = "gas"
    diesel = "diesel"
    

class MLPredictoraspiration(str, Enum):
    std = "std"
    turbo = "turbo"
    

class MLPredictornum_of_doors(str, Enum):
    two = "two"
    four = "four"
    

class MLPredictorbody_style(str, Enum):
    convertible = "convertible"
    hatchback = "hatchback"
    sedan = "sedan"
    wagon = "wagon"
    hardtop = "hardtop"
    

class MLPredictordrive_wheels(str, Enum):
    rwd = "rwd"
    fwd = "fwd"
    FOURwd = "FOURwd"
    

class MLPredictorengine_location(str, Enum):
    front = "front"
    rear = "rear"
    






class MLPredictorengine_type(str, Enum):
    dohc = "dohc"
    ohcv = "ohcv"
    ohc = "ohc"
    l = "l"
    ohcf = "ohcf"
    

class MLPredictornum_of_cylinders(str, Enum):
    four = "four"
    six = "six"
    five = "five"
    three = "three"
    twelve = "twelve"
    eight = "eight"
    


class MLPredictorfuel_system(str, Enum):
    mpfi = "mpfi"
    TWObbl = "TWObbl"
    mfi = "mfi"
    ONEbbl = "ONEbbl"
    spfi = "spfi"
    idi = "idi"
    spdi = "spdi"
    







@app.get("/my_model", tags=['users'])
def predict_my_model(
symboling:int, 
    normalized_losses:float, 
    
    make:MLPredictormake, 
    
    fuel_type:MLPredictorfuel_type, 
    
    aspiration:MLPredictoraspiration, 
    
    num_of_doors:MLPredictornum_of_doors, 
    
    body_style:MLPredictorbody_style, 
    
    drive_wheels:MLPredictordrive_wheels, 
    
    engine_location:MLPredictorengine_location, 
    wheel_base:float, 
    length:float, 
    width:float, 
    height:float, 
    curb_weight:int, 
    
    engine_type:MLPredictorengine_type, 
    
    num_of_cylinders:MLPredictornum_of_cylinders, 
    engine_size:int, 
    
    fuel_system:MLPredictorfuel_system, 
    bore:float, 
    stroke:float, 
    compression_ratio:float, 
    horsepower:float, 
    peak_rpm:float, 
    city_mpg:int, 
    highway_mpg:int
    ):
    args={
    "symboling": symboling,
    "normalized_losses": normalized_losses,
    "make": make,
    "fuel_type": fuel_type,
    "aspiration": aspiration,
    "num_of_doors": num_of_doors,
    "body_style": body_style,
    "drive_wheels": drive_wheels,
    "engine_location": engine_location,
    "wheel_base": wheel_base,
    "length": length,
    "width": width,
    "height": height,
    "curb_weight": curb_weight,
    "engine_type": engine_type,
    "num_of_cylinders": num_of_cylinders,
    "engine_size": engine_size,
    "fuel_system": fuel_system,
    "bore": bore,
    "stroke": stroke,
    "compression_ratio": compression_ratio,
    "horsepower": horsepower,
    "peak_rpm": peak_rpm,
    "city_mpg": city_mpg,
    "highway_mpg": highway_mpg,
    }
    df = pd.DataFrame({k: [v] for k, v in args.items()})
    result = MLPredictor.predict(df, context)
    
    if result.get('error'):
        raise HTTPException(
            status_code=int(result.get('error').get('status_code')), 
            detail=result.get('error').get('detail')
        )

    return result
def _get_values_as_tuple(values: Iterable[str]) -> Tuple[str, ...]:
    return tuple(chain.from_iterable(value.split(",") for value in values))


@app.post("/kedro")
def kedro(
    request: dict = Body(..., example={
        "pipeline_name": "",
        "tag": [],
        "node_names": [],
        "from_nodes": [],
        "to_nodes": [],
        "from_inputs": [],
        "to_outputs": [],
        "params": {}
    })
):
    pipeline_name = request.get("pipeline_name")
    tag = request.get("tag")
    node_names = request.get("node_names")
    from_nodes = request.get("from_nodes")
    to_nodes = request.get("to_nodes")
    from_inputs = request.get("from_inputs")
    to_outputs = request.get("to_outputs")
    params = request.get("params")

    tag = _get_values_as_tuple(tag) if tag else tag
    node_names = _get_values_as_tuple(node_names) if node_names else node_names
    package_name = str(Path(__file__).resolve().parent.name)
    try:
        with KedroSession.create(package_name, env=None, extra_params=params) as session:
            return session.run(
                    tags=tag,
                    node_names=node_names,
                    from_nodes=from_nodes,
                    to_nodes=to_nodes,
                    from_inputs=from_inputs,
                    to_outputs=to_outputs,
                    pipeline_name=pipeline_name,
                )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@app.get("/catalog")
def catalog(
    name: str
):
    try:
        file = context.catalog.load(name)
        return file.to_json(force_ascii=False)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))