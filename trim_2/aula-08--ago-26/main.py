# pip install scikit-learn
# pip install pandas

import numpy as np
from random import shuffle
from sklearn import metrics

from sklearn.datasets import fetch_openml

from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from dataset import data_set

FNAME = '../aula-06--ago-19-trabalho-datasets/mushroom/agaricus-lepiota.data'

data = data_set(FNAME)
xdata = data['dados']
ytarg = data['classes']

media_algoritmos = [0] * 20
for cont in range(20):
        
        # embaralhar os dados
        idx = list(range(len(ytarg)))
        shuffle(idx)
        part = int(len(ytarg)*0.75) # assumindo 75% treino

        # xtr --> x_treino  ;  xte --> x_teste
        xtr = xdata[ :part ]
        ytr = ytarg[ :part ]
        xte = xdata[ part: ]
        yte = ytarg[ part: ]

        rng = np.random.RandomState()

        perceptron = Perceptron(max_iter=100,random_state=rng)
        model_svc = SVC(probability=True, gamma='auto',random_state=rng)
        model_bayes = GaussianNB()
        model_tree = DecisionTreeClassifier(random_state=rng, max_depth=10)
        model_knn = KNeighborsClassifier(n_neighbors=7)

        # colocando todos classificadores criados em um dicionario
        clfs = { 
                'perceptron':   perceptron,
                'svm':          model_svc,
                'bayes':        model_bayes,
                'trees':        model_tree,
                'knn':          model_knn
        }

        acuracia_algoritmos = { 
                'perceptron':   0,
                'svm':          0,
                'bayes':        0,
                'trees':        0,
                'knn':          0
        }

        ytrue = yte
        print('Treinando cada classificador e encontrando o score')
        for clf_name, classific in clfs.items():
                classific.fit(xtr, ytr)
                ypred = classific.predict(xte)
                matrconf = metrics.confusion_matrix(ytrue, ypred)
                acc = metrics.accuracy_score(ytrue, ypred)
                f1 = metrics.f1_score(ytrue, ypred, average='macro')
                print(clf_name, '-- f1:', f1)
                acuracia_algoritmos[clf_name] = f1

        media_algoritmos[cont] = acuracia_algoritmos

