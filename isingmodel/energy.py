import numpy as np
#import random
from isingmodel import configuration

def calculation_of_energy(lattice,energy):
    for i in range(0,4):
        for j in range(0,4):
            energy=energy+lattice[i][j]
print(energy)