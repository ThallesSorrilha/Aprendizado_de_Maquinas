
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from dataset import preprocess_adult_data

FNAME = "../datasets/adult.csv"
# FNAME = "../datasets/mushroom/agaricus-lepiota.csv"


def get_classifiers():

    rng = np.random.RandomState(42)
    return {
        'perceptron': Perceptron(max_iter=100, random_state=rng),
        'svm': SVC(gamma='auto', random_state=rng),
        'bayes': GaussianNB(),
        'tree': DecisionTreeClassifier(random_state=rng, max_depth=10),
        'knn': KNeighborsClassifier(n_neighbors=7)
    }


def main():
    X, y = preprocess_adult_data(FNAME)
    classifiers = get_classifiers()

    f1_scores_per_model = {name: [] for name in classifiers.keys()}

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    print("Iniciando cross-validation com 5 partições...\n")

    for particao, (train_index, test_index) in enumerate(skf.split(X, y)):
        print(f"--- Avaliando na Partição {particao + 1}/5 ---")

        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        for clf_name, clf in classifiers.items():

            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)

            f1 = metrics.f1_score(
                y_test, y_pred, average='macro', zero_division=0)
            f1_scores_per_model[clf_name].append(f1)

            print(f"  {clf_name:<15} - F1-Score: {f1:.4f}")
        print("-" * 30)

    print("\n\n--- Média de F1-Score por Algoritmo (5 partições) ---")
    for clf_name, scores in f1_scores_per_model.items():
        avg_f1 = np.mean(scores)
        print(f"  {clf_name:<15} - F1-Médio: {avg_f1:.4f}")


if __name__ == '__main__':
    main()
