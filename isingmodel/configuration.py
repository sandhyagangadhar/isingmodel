import numpy as np
N=4
initialize_config = np.ones((N, N))
initialize_random_config = 2 * np.random.randint(2, size=(N, N)) - 1


class Configuration2d:
    # def __init__(self):
        # self.array = initialize_config
        # self.a = np.random.randint(0, N)
        # self.b = np.random.randint(0, N)
    def initialize_config(self):
        self.array = np.ones((N, N))
