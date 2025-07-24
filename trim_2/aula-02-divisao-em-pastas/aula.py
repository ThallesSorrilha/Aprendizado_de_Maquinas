
from dataset import data_set

FNAME = '../datasets/adult.csv'

if __name__ == '__main__':
    data = data_set(FNAME)
    for key, value in data.items():
        print(key)

    # atribuindo um novo valor data['dados'],
    # sendo que devem ser inseridas apenas as linhas sem '?'
    data['dados'] = [linha for linha in data['dados'] if '?' not in linha]

    fname = FNAME.split('/')
    fname = fname[-1]
    print('fname -->', fname)

    # dataset retornado - contém nome, dados e classes

    # todo: salvar arquivo contendo dados 'adult--dados.csv'
    # todo: salvar arquivo com todas as classes capturadas 'adult--classes.csv'  
    # todo: remover linhas com números inválidos (inválido: ?)