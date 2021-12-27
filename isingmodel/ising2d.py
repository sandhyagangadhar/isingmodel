import numpy as np
#import random
#from isingmodel import configuration
from isingmodel.metropolis import Metropolis2d
equilibriumsteps = 100000
def get_equilibrium_configuraion():
    for i in range(0,equilibriumsteps):
        Metropolis2d.do_mcmove()
    a2=Metropolis2d
    return(a2.do_mcmove())
print(get_equilibrium_configuraion())









