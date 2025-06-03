import pandas as pd
import numpy as np

def data_set(fname):
    result = {}
    result['nome_arquivo'] = fname
    data = pd.read_csv(fname)
    cols = data.columns
    ultima = cols[-1]  #quando queremos a ultima classe utiliazamos o -1

    nomeOriginal = data[ultima]
    cls_orig, classes = np.unique(nomeOriginal, return_inverse=True)
    conjunto = np.unique(nomeOriginal, return_inverse=True)
    print("Conjunto --> ", conjunto)
    #classes=np.unique(nomeOriginal)
    print('classes --->', classes)

    df = data.drop(columns = ultima)
    print(classes)
    print(df)
    result['dados']= df
    #transoformando as classes em numeros
    

    print(data)
    return result

FNAME = 'iris.csv'
if __name__ == '__main__':
    data = data_set(FNAME)
    print(data)
    print('---'*40)
    print('nome_arquivo ------>',data['nome_arquivo'])