from ..pre_processing.nodes import pre_processing

class MLPredictor:
    def __init__(self, regressor, oe_transformer):
        self.regressor = regressor
        self.oe_transformer = oe_transformer
        
    def predict(self, args_API, context):
        df = args_API
        
        df = df_adjustment(df)
        
        df = pipeline_pp(df)
        df = pipeline_de(df, self.oe_transformer)
        
        prediction = self.regressor.predict(df)
        return {"prediction": prediction[0]}
        

def save_predictor(regressor, oe_transformer):
    predictor = MLPredictor(regressor, oe_transformer)
    return predictor

def df_adjustment(df):
    """This method fixed columns names and values with '_' to '-'
    and the values that start with numbers"""
    columns_name = ['symboling','normalized-losses', 'make',
                    'fuel-type','aspiration','num-of-doors',
                    'body-style','drive-wheels',
                    'engine-location','wheel-base',
                    'length','width','height',
                    'curb-weight','engine-type',
                    'num-of-cylinders','engine-size',
                    'fuel-system','bore','stroke',
                    'compression-ratio','horsepower',
                    'peak-rpm','city-mpg','highway-mpg']
    df = df.set_axis(columns_name, axis='columns', copy=False)    

    columns_enum = [
        'make', 'fuel-type', 
        'aspiration', 'num-of-doors', 
        'body-style', 'drive-wheels', 
        'engine-location', 'engine-type',
        'num-of-cylinders', 'fuel-system'
        ]
    
    for col in columns_enum:
        df[col] = [str(df[col].values[0].split('.')[0])]
    
    if df['make'].values == ['alfa_romero']:
        df['make'] = ['alfa-romero']
    if df['make'].values == ['mercedes_benz']:
        df['make'] = ['mercedes-benz']
    if df['fuel-system'].values == ['TWObbl']:
        df['fuel-system'] = ['2bbl']
    if df['fuel-system'].values == ['ONEbbl']:
        df['fuel-system'] = ['1bbl']
    if df['drive-wheels'].values == ['FOURwd']:
        df['drive-wheels'] = ['4wd']
    
    return df

def pipeline_pp(df):
    df = pre_processing(df)
    return df
    
def pipeline_de(df, oe_transformer):
    columns_to_transform = [
        'make', 'fuel-type', 
        'aspiration', 'num-of-doors', 
        'body-style', 'drive-wheels', 
        'engine-location', 'engine-type',
        'num-of-cylinders', 'fuel-system'
    ]

    df[columns_to_transform]= oe_transformer.transform(df[columns_to_transform])
    
    return df