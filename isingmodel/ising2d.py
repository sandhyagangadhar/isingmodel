from isingmodel.configuration import Configuration2d
from isingmodel.metropolis2d import Metropolis2d
from isingmodel.energyutility import EnergyUtility

NO_OF_EQULIBRIUM_STEPS = 10
MC_STEPS = 10

en=EnergyUtility()
class Ising_2d:
    def get_equilibrium_configuraion(self):
        conf = Configuration2d()
        conf.initialize_config()
        metropolis = Metropolis2d()
        for _ in range(0, NO_OF_EQULIBRIUM_STEPS):
            metropolis.apply(conf)
        return conf

    def calculate_total_energyof_config(self):
        energy = 0.0
        for _ in range(0, MC_STEPS):
            equalibrium_config = self.get_equilibrium_configuraion()
            energy = energy + en.find_total_energy(equalibrium_config.array)
        print(energy / (MC_STEPS * 4 * 4))
ising2d=Ising_2d()
ising2d.calculate_total_energyof_config()





