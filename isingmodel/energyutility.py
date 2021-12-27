class EnergyUtility:
    def __init__(self):
        self.name = "energyutili"
    def find_energy_at_ij(array,i,j):
        nearest_neighbor_sum = (array[i,(j-1)%4]+array[i,(j+1)%4]+array[(i+1)%4,j]+array[(i+j)%4,j])
        energy_after = -1.0*(array[i,j]*nearest_neighbor_sum*array[i,j])
        energy_before = 1.0*(array[i,j]*nearest_neighbor_sum*array[i,j])
        return energy_after,energy_before

    def find_total_energy(accpeted_array):
        energy = 0.0
        for i in range(len(accpeted_array)):
            for j in range(len(accpeted_array)):
                nearest_neighbor_sum_atij = (accpeted_array[i,(j-1)%4]+accpeted_array[i,(j+1)%4]+accpeted_array[(i+1)%4,j]+accpeted_array[(i+j)%4,j])
                energy_at_each_ij = -1.0 * accpeted_array[i, j]
                energy= energy+nearest_neighbor_sum_atij
        return energy








