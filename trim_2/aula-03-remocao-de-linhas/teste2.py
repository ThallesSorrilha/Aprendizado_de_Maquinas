import pandas as pd
import numpy as np

def transform_col(data):
    vlr_orig, values, count = np.unique(data, return_inverse=True, return_counts=True)
    result = {}
    result['values'] = list(values)
    return result['values'] # Return only the numerical representation

def transform_data(data, col_list):
    # Iterate through all columns in the DataFrame
    for colname in data.columns:
        # Check if the column's data type is 'object' (which typically means strings)
        # and if it's not in the col_list (columns to skip transformation)
        if data[colname].dtype == 'object' and colname not in col_list:
            # Apply the transformation and update the column in the DataFrame
            data[colname] = transform_col(data[colname])
    return data

if __name__ == '__main__':
    fname = 'teste2.csv'
    data = pd.read_csv(fname)

    # These are the columns that you *don't* want to transform,
    # so they should remain as strings.
    mystr = 'preco' # Only 'preco' should remain as is
    process = [x.strip() for x in mystr.split(',')]

    # Apply the transformation to string columns not in 'process' list
    # In this case, 'modelo' and 'marca' will be transformed
    data = transform_data(data, process)

    # You no longer need to separate 'classes' or drop the last column
    # as all desired columns are now in 'data' with their transformed values.
    result = {}
    result['dados'] = data # 'data' now holds the transformed DataFrame

    print("---------------")
    print(result['dados'])
    print("---------------")