import pandas as pd
import numpy as np

def _transform_col(data):
    vlr_orig, values, count = np.unique(
        data, return_inverse=True, return_counts=True)
    result = {}
    result['vlr-orig'] = list(vlr_orig)
    result['values'] = list(values)
    result['vlr-count'] = list(count)
    return result

def _transform_data(data, col_list):
    for colname in list(data.columns):
        if colname not in col_list:
            continue
        dados = data[colname]
        ret = _transform_col(dados)
        ret['colname'] = colname
        data.drop(columns=colname)
        data[colname] = ret['values']
    return data

def dataset_info(data):
    data.info(verbose=True)
    print(data.describe())
    print('tipos:', data.dtypes)
    print('dimensoes:', data.ndim)
    print('linhas x colunas:', data.shape)

def data_set(fname):
    result = {}
    result['nome-arquivo'] = fname
    data = pd.read_csv(fname, skipinitialspace=True, skip_blank_lines=True)
    dataset_info(data)

    mystr = 'class,cap-shape,cap-surface,cap-color,bruises,odor,gill-attachment,gill-spacing,gill-size,gill-color,stalk-shape,stalk-root,stalk-surface-above-ring,stalk-surface-below-ring,stalk-color-above-ring,stalk-color-below-ring,veil-type,veil-color,ring-number,ring-type,spore-print-color,population,habitat'
    process = [x.strip() for x in mystr.split(',')]
    data = _transform_data(data, process)

    primeira = data.columns[0]
    classes = list(data[primeira])
    df = data.drop(columns=primeira)

    result['dados'] = df
    result['classes'] = classes

    return result