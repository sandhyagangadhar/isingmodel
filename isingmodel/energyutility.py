import numpy as np
from isingmodel.configuration import Configuration2d


class EnergyUtility:
    def calculate_energy(array,ri,rj):
        sum_pr=0.0
        for i in range(0, 4):
            for j in range(0, 4):
                sum_pr = sum_pr+array[i][j]

        array[ri][rj] = array[ri][rj]*-1.0
        sum_lat=0.0
        for i in range(0, 4):
            for j in range(0, 4):
                sum_lat = sum_lat+array[i][j]
        return sum_pr,sum_lat
