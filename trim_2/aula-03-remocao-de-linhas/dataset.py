
import pandas as pd #importa pandas
import numpy as np #importa numpy


def _transform_col( data ): # função com base em data

    vlr_orig, values, count = np.unique(data, return_inverse=True, return_counts=True) # retorna para cada variável o valor respectivo ao parâmetro: classes em numérico, lista dos dados em classes(numérico), contagem de elementos para cada classe # unique retorna valores únicos
    result = {} # prepara o dicionário de dados
    result['vlr-orig'] = list(vlr_orig) # cria uma lista, a partir de um atributo e carrega no dicionário de dados, pois o valor original é arrayNumpy
    result['values'] = list(values) # ||
    result['vlr-count'] = list(count) # ||
    return result # retorna result - um dicionário de dados


def _transform_data(data, col_list): # função que tem como parâmetro data, e lista de colunas
    for colname in list(data.columns): # chama de colname um elemento da lista de data.columns
        if colname not in col_list: continue # se coluna não está na lista de colunas
        dados = data[ colname ] # dados será os dados que foram passados na posição de colname
        ret = _transform_col( dados ) # transformação de dados -> obtenção de dicionário de dados ret
        ret['colname'] = colname # dicionário de dados ret com base em colname será atribuído colname
        data.drop( columns=colname )
        data[ colname ] = ret['values']

    return data



def dataset_info(data):
    ###################
    data.info(verbose=True)
    print(data.describe())
    print('tipos:', data.dtypes) # tipos de cada uma das colunas
    print('dimensoes:', data.ndim) # número de dimensões
    print('linhas x colunas:', data.shape)
    ###################

def remover_dados_faltantes( df ):
    mascara = df.apply(lambda linha: linha.astype(str).str.contains(r'\?')).any(axis=1) # Converte linha para coluna e compara coluna por coluna, para ver se tem '?'

    # Retorna um DataFrame apenas com as linhas que **não** contêm '?'
    data = df[~mascara].copy()
    return data


def data_set( fname ):
    result = {}
    result['nome-arquivo'] = fname
    data = pd.read_csv(fname, skipinitialspace=True, skip_blank_lines=True)
    dataset_info(data)

    data = remover_dados_faltantes( data )
    # data.to_csv('adult--removido.csv', index=False)
    dataset_info(data)

    mystr = 'workclass, education,  marital-status, occupation,     relationship,   race,   sex,    native-country, class'
    process = [x.strip() for x in mystr.split(',')]
    data = _transform_data(data, process)

    ultima = data.columns[-1]
    classes = list(data[ultima])
    df = data.drop( columns=ultima )

    result['dados'] = df
    result['classes'] = classes

    return result



