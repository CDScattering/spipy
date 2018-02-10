import sys
from spipy.simulate import sim

if __name__=="__main__":
	
	config_default = {'parameters|detd' : 300, 'parameters|lambda' : 2.5, \
                  'parameters|detsize' : 128, 'parameters|pixsize' : 0.3, \
                  'parameters|stoprad' : 10, 'parameters|polarization' : 'x', \
                  'make_data|num_data' : 100, 'make_data|fluence' : 1e14}

	print("Create new project ...")
	sim.generate_config_files(pdb_file='./1N0U1.pdb', workpath=None, name='simu_test', params=config_default)
	
	print("Simulating ...")
	sim.run_simulation()
