import numpy as np
size=4


class Configuration2d:
    def __init__(self):
        self.array = np.ones((size, size))

    def change_spin_at_random_position(self):
        i = np.random.randint(0, size)
        j = np.random.randint(0, size)
        self.array[i][j] = self.array[i][j] * -1.0

# a1=Configuration2d
# print(a1.find_randomposition_of_lattice_2d())

