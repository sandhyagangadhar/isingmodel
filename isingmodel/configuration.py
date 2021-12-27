import numpy as np
size=4
initialize_config = np.ones((size, size))

class Configuration2d:
    def __init__(self):
        self.array = initialize_config
        self.a = np.random.randint(0, size)
        self.b = np.random.randint(0, size)


