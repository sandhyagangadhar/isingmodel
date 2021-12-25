import numpy as np
size=4


class Configuration2d:
    def __init__(self):
        self.array = np.ones((size, size))
        self.i = np.random.randint(0, size)
        self.j = np.random.randint(0, size)


