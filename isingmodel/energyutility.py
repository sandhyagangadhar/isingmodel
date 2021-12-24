import numpy as np
from isingmodel.configuration import Configuration2d


class EnergyUtility:
    def calculate_energy(array):
        sum = 0.0
        for i in range(0, 4):
            for j in range(0, 4):
                sum = sum + array[i][j]
        return sum
