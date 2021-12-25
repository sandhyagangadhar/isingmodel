import numpy as np
from isingmodel.configuration import Configuration2d
from isingmodel.energyutility import EnergyUtility


class Metropolis2d:
    def apply_metropolis():
        conf = Configuration2d()
        print(conf.i,conf.j)
        energy_later,energy_before=EnergyUtility.find_energy_at_ij(conf.array,conf.i,conf.j)
        print('energy_later,energy_before',energy_later,energy_before)
        energy_diff = (energy_later)-(energy_before)
        if(energy_diff>=0):
            conf.array[conf.i][conf.j] = conf.array[conf.i][conf.j] * -1.0
            print(conf.array)
    #    elif():
     #       print(np.random())
        else:
            print(np.exp(-energy_diff))





a2=Metropolis2d
a2.apply_metropolis()





