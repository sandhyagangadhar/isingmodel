import numpy as np
from math import radians, cos, sin, asin, sqrt
#array=np.ones((3,3))
#print(array)
size=4
class Initial_configuration:
    def __init__(self, size):
        self.array=np.ones((size,size))

def configuration():
    a = Initial_configuration(size)
    print(a.array[0][1])
configuration()





