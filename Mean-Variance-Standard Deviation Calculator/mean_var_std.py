import numpy as np


def calculate(digits_list):

    if len(digits_list) != 9:
        raise ValueError('List must contain nine numbers.')

    # Initializing the output
    calculations = {}

    # Converting the list into a 3x3 numpy array
    array = np.array(digits_list).reshape(3,3)

    # Calculating the mean
    calculations['mean'] = [
        np.mean(array, axis=0).tolist(),
        np.mean(array, axis=1).tolist(),
        np.mean(array)
    ]

    # Calculating the variance
    calculations['variance'] = [
        np.var(array, axis=0).tolist(),
        np.var(array, axis=1).tolist(),
        np.var(array).tolist(),
    ]

    # Calculating the standard deviation
    calculations['standard deviation'] = [
        np.std(array, axis=0).tolist(),
        np.std(array, axis=1).tolist(),
        np.std(array).tolist(),
    ]

    # Calculating the max
    calculations['max'] = [
        np.amax(array, axis=0).tolist(),
        np.amax(array, axis=1).tolist(),
        np.amax(array).tolist()
    ]

    # Calculating the min
    calculations['min'] = [
        np.amin(array, axis=0).tolist(),
        np.amin(array, axis=1).tolist(),
        np.amin(array).tolist()
    ]

    # Calculating the sum
    calculations['sum'] = [
        np.sum(array, axis=0).tolist(),
        np.sum(array, axis=1).tolist(),
        np.sum(array).tolist()
    ]

    return calculations
