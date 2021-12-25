import numpy as np
size=4
array = np.ones((size, size))

class Configuration2d:
    def __init__(self):
        self.array = array
        self.a = np.random.randint(0, size)
        self.b = np.random.randint(0, size)


