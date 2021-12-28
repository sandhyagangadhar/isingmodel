import numpy as np

LATTICE_SIZE = 4


class Configuration2d:

    def initialize_config(self, random=False):
        if random:
            self.array = 2 * np.random.randint(2, size=(LATTICE_SIZE, LATTICE_SIZE)) - 1
        else:
            self.array = np.ones((LATTICE_SIZE, LATTICE_SIZE))
