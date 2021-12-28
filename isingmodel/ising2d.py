from isingmodel.configuration import Configuration2d
from isingmodel.metropolis import Metropolis2d
#from isingmodel.configuration import Configuration2d
from isingmodel.energyutility import EnergyUtility

equilibriumsteps = 100
MC_STEPS = 10
a2 = Metropolis2d()
en=EnergyUtility()
class Ising_2d:
    def get_equilibrium_configuraion(self):
        conf = Configuration2d()
        conf.initialize_config()
        for _ in range(0, equilibriumsteps):
            a2.apply_metropolis(conf)
        return conf

    def calculate_total_energyof_config(self):
        energy = 0.0
        for _ in range(0, MC_STEPS):
            equalibrium_config = self.get_equilibrium_configuraion()
            energy = energy + en.find_total_energy(equalibrium_config.array)
        print(energy / (MC_STEPS * 4 * 4))
ising2d=Ising_2d()
ising2d.calculate_total_energyof_config()




# listT={0.5,0.7,0.9,1.0}
# def find_energy_at_each_temp():
#     for temp in range(listT):
#



