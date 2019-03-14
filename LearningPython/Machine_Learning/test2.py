#read in Data

import scipy as sp
import numpy as np

data = sp.genfromtxt("data1.txt", dtype=str, delimiter="\n")
print(data.shape)
print(data)

a = np.array([1,2,3,4])
print(a.shape)
