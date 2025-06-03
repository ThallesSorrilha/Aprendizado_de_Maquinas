import numpy as np
import pandas as pd

with open('ex_flores/flores.csv', 'r') as file:
    tmp = np.fromfile(file)

#tmp = np.array(tmp)
# [linhas,colunas]
# 1ºelem. : ult.elem.
tmp = tmp[ : , -1]
unq = np.unique(tmp)

print('unique -->', unq)