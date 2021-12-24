import numpy as np
from isingmodel.configuration import Configuration2d
from isingmodel.energyutility import EnergyUtility


class Metropolis2d:
    def apply_metropolis():
        conf = Configuration2d()
        print(conf.i,conf.j)
        print(conf.array)
        energy_previous,energy_later=EnergyUtility.calculate_energy(conf.array,conf.i,conf.j)
        print('energy_previous,energy_later',energy_previous,energy_later)
   #     conf.change_spin_at_random_position()
    #    energy_later = EnergyUtility.calculate_energy(conf.array,conf.i,conf.j)
   #     print('energy_later',energy_later)
        if(energy_later<energy_previous):
            print(conf.array)
        else:
            conf.array[conf.i][conf.j]=conf.array[conf.i][conf.j]*-1.0
            print(conf.array)



a2=Metropolis2d
a2.apply_metropolis()
#a2 = configuration.Configuration2d()





