import numpy as np
from numpy.random import rand
from isingmodel.configuration import Configuration2d
from isingmodel.energyutility import EnergyUtility


class Metropolis2d:
    def apply_metropolis():
        a2=0
        for i in range(0,1000):
            conf = Configuration2d()
            energy_later, energy_before = EnergyUtility.find_energy_at_ij(conf.array, conf.a, conf.b)
            energy_diff = (energy_later) - (energy_before)
            if (energy_diff < 0.0):
                conf.array[conf.a][conf.b] = conf.array[conf.a][conf.b] * -1.0
            else:
                a2=a2+1
               # print(rand() * 1000)
               # print(np.exp(-energy_diff) * 0.5)





a2=Metropolis2d
a2.apply_metropolis()





