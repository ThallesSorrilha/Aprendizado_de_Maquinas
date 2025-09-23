import pandas as pd
import numpy as np

# age, workclass, final_weight, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country, class

# age: continuous.
# workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
# final_weight: continuous. (final_weight)
# education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
# education-num: continuous.
# marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
# occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
# relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
# race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
# sex: Female, Male.
# capital-gain: continuous.
# capital-loss: continuous.
# hours-per-week: continuous.
# native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.

FNAME = '../datasets/adult.csv'
REMOCAO = ['capital-gain', 'capital-loss']
NORMALIZ = ['age', 'final_weight', 'education-num']
CATEGORIZ = ['workclass', 'education', 'marital-status', 'occupation',
             'relationship', 'race', 'sex', 'hours-per-week', 'native-country', 'class']


def categoriz_col(data):
    _, values = np.unique(data, return_inverse=True)
    return list(values)


def normalize_col(data):
    min_val = data.min()
    max_val = data.max()
    if max_val != min_val:
        data = (data - min_val) / (max_val - min_val)
    else:
        data = 0
    return data


def load_dataset(fname, normaliz=None, categoriz=None, remocao=None):
    data = pd.read_csv(fname, skipinitialspace=True, skip_blank_lines=True)
    if remocao:
        data.drop(columns=remocao, inplace=True)
    data.replace('?', np.nan, inplace=True)
    data.dropna(inplace=True)
    if normaliz:
        for col in normaliz:
            data[col] = normalize_col(data[col])
    if categoriz:
        for col in categoriz:
            data[col] = categoriz_col(data[col])


if __name__ == '__main__':
    data = load_dataset(FNAME, normaliz=NORMALIZ,
                        categoriz=CATEGORIZ, remocao=REMOCAO)
