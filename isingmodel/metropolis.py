import numpy as np
from isingmodel import configuration

class Metropolis2d:
    def applying_metropolis():
        a1=configuration.Configuration2d
        energy_previous=(a1.calculation_of_energy())
        a1.finding_randomposition_of_lattice_2d()
        energy_later = (a1.calculation_of_energy())





