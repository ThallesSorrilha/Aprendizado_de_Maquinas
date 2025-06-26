import pandas as pd
import numpy as np

def transforma_valores( data, coluna ):
    valor = data[ coluna ]
    vlr_orig, vlr, count = np.unique(valor, return_inverse=True, return_counts=True)
    data[ coluna ] = vlr
    return data, vlr_orig, vlr, count


def data_set_v2( fname ):
    result = {}
    result['nome-arquivo'] = fname

    data = pd.read_csv(fname, skipinitialspace=True)
    process = ['workclass', 'native-country', 'education', 'marital-status', 'class']

    info = {}
    for colname in process:
        data, orig, classes, cnt = transforma_valores( data, colname )
        info[colname] = {
            'orig': orig,
            'classes': classes,
            'count': cnt
        }

    result['dados'] = data.drop(columns='class')
    result['classes'] = info['class']['classes']
    result['cls-orig'] = info['class']['orig']
    result['cls-count'] = info['class']['count']

    return result


def data_set( fname ):
    result = {}
    result['nome-arquivo'] = fname
    data = pd.read_csv(fname)
    cols = data.columns
    ultima = cols[-1]

    nome_orig = data[ultima]

    cls_orig, classes, cls_cnt = np.unique(nome_orig, return_inverse=True, return_counts=True)

    df = data.drop( columns=ultima )

    result['dados'] = df
    result['classes'] = classes
    result['cls-orig'] = cls_orig
    result['cls-count'] = cls_cnt

    return result


def mostra_dados( data ):
    print('-'*40)
    ncls = len( data['cls-orig'] )
    print(f'1- possui {ncls} classes')
    print('2- numero de itens para cada classe:', data['cls-count'])
    print('-'*40)

def mostra_desbalanceamento( data ):
    soma = np.sum( data['cls-count'] )
    result = []
    for vlr in data['cls-count']:
        result.append( soma / vlr )

    max = np.max( result )
    print('desbalanceamento -->', max)


FNAME = 'trim_2/aula_01-gerenciamento_de_dados/adult.csv'

if __name__ == '__main__':
    data = data_set_v2(FNAME)
    mostra_dados( data )
    mostra_desbalanceamento( data )