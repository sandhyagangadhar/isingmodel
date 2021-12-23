import numpy as np
#import random
from isingmodel import configuration
from isingmodel import energy
size = 4
lattice=np.ones((size,size))
energy=0.0
def finding_random_position(lattice):
    configuration.lattice(lattice)
    i=np.random.randint(0, size)
    j=np.random.randint(0, size)
    lattice[i][j]= lattice[i][j]*-1.0
finding_random_position(lattice)
energy.calculation_of_energy(lattice,energy)




