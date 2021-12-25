import numpy as np
from numpy.random import rand
from isingmodel.configuration import Configuration2d
from isingmodel.energyutility import EnergyUtility

list_temp = [0.2,0.5,0.8,1.0]
class Metropolis2d:
    def apply_metropolis():
        for Temp in list_temp:
            for i in range(0, 10):
                conf = Configuration2d()
                energy_later, energy_before = EnergyUtility.find_energy_at_ij(conf.array, conf.a, conf.b)
                energy_diff = (energy_later) - (energy_before)
                if (energy_diff < 0.0):
                    conf.array[conf.a][conf.b] = conf.array[conf.a][conf.b] * -1.0
                elif (rand() < np.exp((-1.0 * energy_diff)/Temp)):
                    conf.array[conf.a][conf.b] = conf.array[conf.a][conf.b] * -1.0
                else:
                    conf.array[conf.a][conf.b] = conf.array[conf.a][conf.b]

a2=Metropolis2d
a2.apply_metropolis()





