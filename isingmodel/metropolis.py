import numpy as np
from numpy.random import rand
class Metropolis:
    def acceptance_under_permissible_probability(self,energy_diff):
        return rand() < np.exp((-1.0 * energy_diff) / 0.5)