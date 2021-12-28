import numpy as np
from numpy.random import rand
from isingmodel.configuration import Configuration2d, LATTICE_SIZE
from isingmodel.energyutility import EnergyUtility

class Metropolis2d:
    def apply(self, conf):
        energy = 0.0
        for i in range(0, LATTICE_SIZE):
            for j in range(0, LATTICE_SIZE):
                randomI = np.random.randint(0, LATTICE_SIZE)
                randomJ = np.random.randint(0, LATTICE_SIZE)
                energy_diff = EnergyUtility().find_energy_diff_at_ij(conf.array, randomI,randomJ)
                if energy_diff < 0.0 or self.acceptance_under_permissible_probability(energy_diff):
                    self.accept_configuration(conf.array,randomI,randomJ)

    def accept_configuration(self,array,randomI,randomJ):
        array[randomI][randomJ] = array[randomI][randomJ] * -1.0

    def acceptance_under_permissible_probability(self,energy_diff):
        return rand() < np.exp((-1.0 * energy_diff) / 0.5)

