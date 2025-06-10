import pandas as pd
import numpy as np

def data_set(name):
    result = {}
    result['nome-arquivo'] = name
    data = pd.read_csv(name)
    cols = data.columns
    ultima = cols[-1]

    nome_orig = data[ultima]
    cls_orig, classes, cls_cnt = np.unique(nome_orig, return_inverse=True, return_counts=True)

    print("classes 1: ", classes)

    result['classes'] = classes
    result['cls-orig'] = cls_orig
    result['cls-cnt'] = cls_cnt

    return result

FNAME = 'iris.csv'

# with open('iris.csv', 'r') as file:
#     tmp = np.loadtxt(file)
#     print(tmp)

if __name__ == '__main__':
    data = data_set(FNAME)
    print('-' * 40)

    for key, value in data.items():
        print(f'{key} : {value}')

    print('nome-arquivo: ', data['nome-arquivo'])
    print(data['cls-orig'])
    print(data['cls-cnt'])
    print(data['classes'])
    ncls = len(data['cls-orig'])
    print(f'1 - possui {ncls} classes')
    print(f'2 - número de itens  para cada classe: ', data['cls-cnt'])

    print("*" * 40)
    soma = np.sum(data['cls-cnt'])
    result = []
    for vlr in data['cls-cnt']:
        result.append(soma / vlr)

    max = np.max(result)
    print("valor máximo: ", max)