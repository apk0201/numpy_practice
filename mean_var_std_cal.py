import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    l1 = list[0:3]
    l2 = list[3:6]
    l3 = list[6:]
    new_list = [l1, l2, l3]
    arr = np.array(new_list)
    flattened = arr.flatten(order='A')
    axis0_sum = arr.sum(axis=0)
    axis1_sum = arr.sum(axis=1)
    axis0_mean = arr.mean(axis=0)
    axis1_mean = arr.mean(axis=1)
    axis0_var = arr.var(axis=0)
    axis1_var = arr.var(axis=1)
    axis0_std = arr.std(axis=0)
    axis1_std = arr.std(axis=1)
    axis0_max = arr.max(axis=0)
    axis1_max = arr.max(axis=1)
    axis0_min = arr.min(axis=0)
    axis1_min = arr.min(axis=1)
    calculations = {'mean': [axis0_mean.tolist(), axis1_mean.tolist(), flattened.mean(axis=0)],
                    'variance': [axis0_var.tolist(), axis1_var.tolist(), flattened.var(axis=0)],
                    'standard deviation': [axis0_std.tolist(), axis1_std.tolist(), flattened.std(axis=0)],
                    'max': [axis0_max.tolist(), axis1_max.tolist(), flattened.max(axis=0)],
                    'min': [axis0_min.tolist(), axis1_min.tolist(), flattened.min(axis=0)],
                    'sum': [axis0_sum.tolist(), axis1_sum.tolist(), flattened.sum(axis=0)]}
    return calculations


print(calculate([0,1,2,3,4,5,6,7,8]))
