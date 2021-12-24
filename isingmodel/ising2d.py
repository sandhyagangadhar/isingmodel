import numpy as np
#import random
from isingmodel import configuration
#from isingmodel import energy

a1=configuration.Configuration2d
print(a1.calculate_energy())
print(a1.change_spin_at_random_position())



