import pandas as pd
import numpy as np

fname = 'teste.csv'
data = pd.read_csv(fname, header=None)
mascara = [0] * 10
mascara = np.array(mascara, dtype=bool)

mascara[ [3,6,9] ] = True

df = data[mascara]
print(df)