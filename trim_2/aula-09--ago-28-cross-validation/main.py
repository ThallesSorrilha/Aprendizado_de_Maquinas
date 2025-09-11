# pip install scikit-learn
# pip install pandas

import numpy as np
from random import shuffle
from sklearn import metrics
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from dataset import data_set

# Dataset file path
FNAME = '../aula-06--ago-19-trabalho-datasets/mushroom/agaricus-lepiota.data'

def load_and_shuffle_data(fname):
    """Carrega o dataset e o embaralha uma única vez."""
    data = data_set(fname)
    xdata = np.array(data['dados'])
    ytarg = np.array(data['classes'])
    
    # Embaralha os dados
    idx = list(range(len(ytarg)))
    shuffle(idx)
    
    return xdata[idx], ytarg[idx]

def build_classifiers():
    """Cria e retorna os classificadores a serem avaliados."""
    rng = np.random.RandomState(42) # Usando seed para reprodutibilidade
    
    return {
        'perceptron': Perceptron(max_iter=100, random_state=rng),
        'svm': SVC(gamma='auto', random_state=rng),
        'bayes': GaussianNB(),
        'tree': DecisionTreeClassifier(random_state=rng, max_depth=10),
        'knn': KNeighborsClassifier(n_neighbors=7)
    }

def cross_validate_and_evaluate(xdata, ytarg, k_folds=5):
    """Executa a validação cruzada com k folds e retorna as pontuações F1."""
    classifiers = build_classifiers()
    f1_scores = {name: [] for name in classifiers.keys()}
    fold_size = len(ytarg) // k_folds
    
    print(f"Executando validação cruzada com {k_folds} folds.\n")

    for i in range(k_folds):
        print(f'--- Avaliando no Fold {i+1}/{k_folds} ---')
        
        # Define os índices para treino e teste
        test_start = i * fold_size
        test_end = test_start + fold_size
        
        test_indices = list(range(test_start, test_end))
        train_indices = list(range(len(ytarg)))
        
        for idx in sorted(test_indices, reverse=True):
            train_indices.pop(idx)
        
        # Particiona os dados
        xtr, ytr = xdata[train_indices], ytarg[train_indices]
        xte, yte = xdata[test_indices], ytarg[test_indices]
        
        # Treina e avalia cada classificador
        for clf_name, clf in classifiers.items():
            clf.fit(xtr, ytr)
            ypred = clf.predict(xte)
            
            f1 = metrics.f1_score(yte, ypred, average='macro', zero_division=0)
            f1_scores[clf_name].append(f1)
            
            print(f"  {clf_name:<15} - F1-Score: {f1:.4f}")
        print("-" * 30)

    return f1_scores

def display_results(f1_scores):
    """Exibe os resultados finais de forma organizada."""
    print("\n\n--- Resultados Finais (Média F1-Score) ---")
    for clf_name, scores in f1_scores.items():
        average_f1 = np.mean(scores)
        print(f"  {clf_name:<15} - F1-Médio: {average_f1:.4f}")

if __name__ == '__main__':
    xdata_shuffled, ytarg_shuffled = load_and_shuffle_data(FNAME)
    all_f1_scores = cross_validate_and_evaluate(xdata_shuffled, ytarg_shuffled)
    display_results(all_f1_scores)