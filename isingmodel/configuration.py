import numpy as np
size=4
array=np.ones((size, size))
#print(array)
class Configuration2d:
    def __init__(self, array):
        self.array = array
    def finding_randomposition_of_lattice_2d():
        i = np.random.randint(0, size)
        j = np.random.randint(0, size)
        array[i][j] = array[i][j] * -1.0
        return array
    def calculation_of_energy():
        sum=0.0
        for i in range(0,4):
            for j in range(0,4):
                sum=sum+array[i][j]
        return sum
#a1=Configuration2d
#print(a1.calculation_of_energy())

#print(a1.array)
#class Configuration2d:
 #   def lattice_2d(self, array):
  #      self.array = array
   #     i = np.random.randint(0, size)
    #    j = np.random.randint(0, size)
     #   self.array[i][j] = self.array[i][j] * -1.0
 #   def __init__(self, size):
  #      self.array=np.ones((size,size))
#a = Configuration2d()
#print(a.array)

#def lattice(a):
 #   a = Initiallattice(size)
  #  print()
#def finding_random_position(lattice):
 #   i=np.random.randint(0, size)
  #  j=np.random.randint(0, size)
   # lattice[i][j]= lattice[i][j]*-1.0
