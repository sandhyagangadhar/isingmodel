import numpy as np
from isingmodel.configuration import Configuration2d


class EnergyUtility:
    def find_energy_at_ij(array,i,j):
        nearest_neighbor_sum = (array[i,(j-1)%4]+array[i,(j+1)%4]+array[(i+1)%4,j]+array[(i+j)%4,j])
        energy_after = -1.0*array[i,j]*nearest_neighbor_sum*array[i,j]
        energy_before = 1.0*array[i,j]*nearest_neighbor_sum*array[i,j]
        return energy_after,energy_before


