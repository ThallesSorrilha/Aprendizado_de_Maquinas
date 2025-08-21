
from dataset import data_set

FNAME = '../datasets/adult.csv'

'''def gerarArquivos(dados):
    n = len(dados)
    split_idx = int(n * 0.8)

    geral = dados
    x_treino = [linha[:-1] for linha in dados[:split_idx]]
    y_treino = [linha[-1] for linha in dados[:split_idx]]
    x_teste = [linha[:-1] for linha in dados[split_idx:]]
    y_teste = [linha[-1] for linha in dados[split_idx:]]'''

if __name__ == '__main__':
    data = data_set(FNAME)
    for key, value in data.items():
        print(key)
    fname = FNAME.split('/')
    fname = fname[-1]
    print('fname -->', fname) 
