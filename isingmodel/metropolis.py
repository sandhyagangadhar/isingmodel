import numpy as np
from numpy.random import rand
from isingmodel.configuration import Configuration2d
from isingmodel.energyutility import EnergyUtility
size = 4
class Metropolis2d:
    def __init__(self):
        self = "abc"
    def do_mcmove():
        energy = 0.0
        for i in range(0, size):
            for j in range(0, size):
                conf = Configuration2d()
            energy_later, energy_before = EnergyUtility.find_energy_at_ij(conf.array, conf.a, conf.b)
            energy_diff = (energy_later) - (energy_before)
            if (energy_diff < 0.0):
                conf.array[conf.a][conf.b] = conf.array[conf.a][conf.b] * -1.0
                energy = energy + EnergyUtility.find_total_energy(conf.array)
            elif (rand() < np.exp((-1.0 * energy_diff) / 0.5)):
                conf.array[conf.a][conf.b] = conf.array[conf.a][conf.b] * -1.0
                energy = energy + EnergyUtility.find_total_energy(conf.array)
            else:
                conf.array[conf.a][conf.b] = conf.array[conf.a][conf.b]
        return(conf.array)


a2 = Metropolis2d
#print(a2.do_mcmove())
