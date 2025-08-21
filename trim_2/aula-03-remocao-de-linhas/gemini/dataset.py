import pandas as pd
import numpy as np

def _transform_col(data):
    # Retorna diretamente o array de valores numéricos
    vlr_orig, values, count = np.unique(data, return_inverse=True, return_counts=True)
    return list(values)

def _transform_data(data, col_list):
    # Garante que os nomes das colunas não tenham espaços
    data.columns = data.columns.str.strip()
    
    for colname in data.columns:
        # Apenas transforma as colunas que estão na lista `col_list`
        if colname in col_list:
            dados = data[colname]
            # Atribui os novos valores numéricos à coluna
            data[colname] = _transform_col(dados)
    return data

def dataset_info(data):
    print("--- Informações do Dataset ---")
    data.info(verbose=True)
    print("\n--- Estatísticas Descritivas ---")
    print(data.describe())
    print("\n--- Tipos de Dados ---")
    print(data.dtypes)
    print("\n--- Dimensões ---")
    print('dimensoes:', data.ndim)
    print('linhas x colunas:', data.shape)
    print("--------------------------------")

def remover_dados_faltantes(df):
    mascara = df.apply(lambda linha: linha.astype(str).str.contains(r'\?')).any(axis=1)
    data = df[~mascara].copy()
    return data

def data_set(fname):
    print(f"Lendo o arquivo: {fname}")
    result = {}
    result['nome-arquivo'] = fname
    
    data = pd.read_csv(fname, skipinitialspace=True, skip_blank_lines=True)
    print("--- Dataset Original ---")
    dataset_info(data)

    data = remover_dados_faltantes(data)
    print("\n--- Dataset após remover dados faltantes ---")
    dataset_info(data)

    mystr = 'workclass, education, marital-status, occupation, relationship, race, sex, native-country, class'
    process = [x.strip() for x in mystr.split(',')]
    
    # Aplica a transformação apenas nas colunas listadas em 'process'
    data = _transform_data(data, process)

    # Separa a última coluna (classes) do restante do DataFrame
    ultima = data.columns[-1]
    classes = list(data[ultima])
    df = data.drop(columns=ultima)

    result['dados'] = df
    result['classes'] = classes

    return result