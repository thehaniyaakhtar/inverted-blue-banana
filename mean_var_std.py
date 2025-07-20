import numpy as np

def calculate(list):
    #ensure there are 9 numbers on the list
    if len(list) != 9:
        #raise value error if condition is not met
        raise ValueError("List must contain nine numbers.")
    
    #convert list to 3x3 array
    array = np.array(list).reshape(3, 3)

    #calculations
    calculations = {
        'mean': [array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), array.mean().item()],
        'variance': [array.var(axis=0).tolist(), array.var(axis=1).tolist(), array.var().item()],
        'standard deviation': [array.std(axis=0).tolist(), array.std(axis=1).tolist(), array.std().item()],
        'max': [array.max(axis=0).tolist(), array.max(axis=1).tolist(), array.max().item()],
        'min': [array.min(axis=0).tolist(), array.min(axis=1).tolist(), array.min().item()],
        'sum': [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), array.sum().item()]
    }


    return calculations
