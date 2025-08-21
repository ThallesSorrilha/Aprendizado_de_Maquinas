# pip install scikit-learn
# pip install pandas

from sklearn.linear_model import Perceptron
from sklearn import metrics
from random import shuffle
import numpy as np

from dataset import data_set

FNAME = '../aula-06--ago-19-trabalho-datasets/mushroom/agaricus-lepiota.data'


def run():
    data = data_set(FNAME)
    xdata = data['dados']
    ytarg = data['classes']

    xdata = np.array(xdata)  # np.array -> para embaralhar dados
    ytarg = np.array(ytarg)

    # embaralhar os dados
    nums = list(range(len(ytarg)))
    shuffle(nums)

    xdata = xdata[nums]
    ytarg = ytarg[nums]

    size = len(ytarg)
    particao = int(size*0.6)  # treino -> 60%

    xtreino = xdata[: particao]
    ytreino = ytarg[: particao]

    xteste = xdata[particao:]
    yteste = ytarg[particao:]

    perceptron = Perceptron(max_iter=100, random_state=42)
    perceptron.fit(xtreino, ytreino)
    yhat = perceptron.predict(xteste)

    score = metrics.accuracy_score(yteste, yhat)
    matrix = metrics.confusion_matrix(yteste, yhat)

    tn, fp, fn, tp = matrix.ravel()
    print(f'TN: {tn}, FP: {fp}, FN: {fn}, TP: {tp}')

    acuracia = (tp + tn) / (tp + tn + fp + fn)
    print(f'Acurácia: {acuracia}')
    precisao = tp / (tp + fp)
    print(f'Precisão: {precisao}')
    recall = tp / (tp + fn)
    print(f'Recall: {recall}')

    f1 = (2 * precisao * recall) / (precisao + recall)
    print(f'F1: {f1}')

    resultado = {'score': score, 'f1': f1}
    return resultado


scores = []
f1s = []
for idx in range(20):
    print(f'executando indice [{idx}]')
    resposta = run()

    scores.append(resposta['score'])
    f1s.append(resposta['f1'])

print(f'Acurácia média:{np.average(scores)}')
print(f'F1 médio:{np.average(f1s)}')
