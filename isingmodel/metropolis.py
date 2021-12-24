import numpy as np
from isingmodel.configuration import Configuration2d
from isingmodel.energyutility import EnergyUtility


class Metropolis2d:
    def apply_metropolis():
        conf = Configuration2d()
        energy_previous=EnergyUtility.calculate_energy(conf.array)
        print('energy_previous',energy_previous)
        prevArray = conf.array
        conf.change_spin_at_random_position()
        energy_later = EnergyUtility.calculate_energy(conf.array)
        print('energy_later',energy_later)
        if(energy_later>energy_previous):
            print(conf.array)



a2=Metropolis2d
a2.apply_metropolis()
#a2 = configuration.Configuration2d()





