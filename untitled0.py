# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

######  Example 1.11 ##########
# load text file
fname = 'Sales_01_20.csv' # comma separated values
data1 = np.loadtxt(fname, delimiter=',', skiprows=1)
result_dict = {}
for sublist in data1:
    key = sublist[0]
    value = sublist[1]
    if key in result_dict:
        result_dict[key].append(value)
    else:
        result_dict[key] = [value]
meandic={}
for key in result_dict:
    values =result_dict[key]
    mean=np.mean(np.array(values))
    meandic[key]=mean
print(meandic)