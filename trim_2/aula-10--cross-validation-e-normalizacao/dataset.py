import pandas as pd
import numpy as np

def preprocess_adult_data(fname):

    data = pd.read_csv(fname, skipinitialspace=True)
    
    data.drop(columns=['capital-gain', 'capital-loss'], inplace=True)
    
    data.replace('?', np.nan, inplace=True)
    data.dropna(inplace=True)
    
    continuous_cols = ['age', 'final_weight', 'education-num', 'hours-per-week']
    categorical_cols = [
        'workclass', 'education', 'marital-status', 'occupation', 
        'relationship', 'race', 'sex', 'native-country', 'class'
    ]
    
    for col in continuous_cols:
        min_val = data[col].min()
        max_val = data[col].max()
        if max_val != min_val:
            data[col] = (data[col] - min_val) / (max_val - min_val)
        else:
            data[col] = 0
    
    for col in categorical_cols:
        data[col], _ = pd.factorize(data[col])
        
    X = data.drop(columns='class').values
    y = data['class'].values
    
    return X, y