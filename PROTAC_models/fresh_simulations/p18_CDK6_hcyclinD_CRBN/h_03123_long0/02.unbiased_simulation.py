import os
from pdbfixer import PDBFixer
import simtk.openmm as mm
from simtk.openmm import unit, version, Context, MonteCarloBarostat, XmlSerializer
from simtk.openmm.app import PDBFile, PME, Simulation, StateDataReporter, HBonds, AmberPrmtopFile, AmberInpcrdFile
from mdtraj.reporters import NetCDFReporter

# set up basic parameters
experiment = 'p18_CDK6_hcyclinD_CRBN'
receptor = 'CDK6'
ligand = '03123'
trial = 0
work_dir = f'/home/guoj1/data_projects/BSJ_inhibitors/fresh_simulations/{experiment}/h_{ligand}_long{trial}'
temperature = 400.15 * unit.kelvin
pressure = 1.0 * unit.atmospheres
steps = 250000000 ## 1000 ns

# load prm or crd files of the minimized and equilibrated protein 
prmtop = AmberPrmtopFile(f'../03123_long0/complex_prep/02.ante.tleap/{ligand}_{receptor}.com.wat.leap.prmtop')
pdb = PDBFile(f'../03123_long0/{ligand}_{receptor}_holo_equi.pdb')

print("OpenMM version:", version.version)
# use heavy hydrogens and constrain all hygrogen atom-involved bonds
system = prmtop.createSystem(nonbondedMethod=PME, rigidWater=True, nonbondedCutoff=1 * unit.nanometer, constraints = HBonds, removeCMMotion=False, hydrogenMass= 4 * unit.amu)
system.addForce(MonteCarloBarostat(pressure, temperature))

# Set up the context for unbiased simulation
integrator = mm.LangevinIntegrator(temperature, 1.0, 0.004) ## 4 fs time steps
integrator.setRandomNumberSeed(trial)
print(f"Random seed of this run is: {integrator.getRandomNumberSeed()}")
platform = mm.Platform.getPlatformByName('OpenCL')
print("Done specifying integrator and platform for simulation.")
platform.setPropertyDefaultValue('Precision', 'mixed')
print("Done setting the precision to mixed.")

simulation = Simulation(prmtop.topology, system, integrator, platform)
simulation.context.setPositions(pdb.positions)
print("Done recording a context for positions.")
context = simulation.context
context.setVelocitiesToTemperature(temperature)
print("Done assigning velocities.")
storage_path = os.path.join(work_dir,'traj.nc')
#potential_path = os.path.join(work_dir,'potential.txt')
simulation.reporters.append(NetCDFReporter(storage_path, reportInterval=250000, coordinates=True))
#simulation.reporters.append(StateDataReporter(potential_path, 1, step=True, potentialEnergy=True))
print("Done specifying simulation.")
simulation.step(steps)

# Serialize state
print('Serializing state to state.xml...')
state = context.getState(getPositions=True, getVelocities=True, getEnergy=True, getForces=True)
with open('state.xml', 'w') as outfile:
    xml = XmlSerializer.serialize(state)
    outfile.write(xml)

# Serialize system
print('Serializing System to system.xml...')
system.setDefaultPeriodicBoxVectors(*state.getPeriodicBoxVectors())
with open('system.xml', 'w') as outfile:
    xml = XmlSerializer.serialize(system)
    outfile.write(xml)

print(f"Done with {steps} steps of simulation.")
print('  final   : %8.3f kcal/mol' % (context.getState(getEnergy=True).getPotentialEnergy()/unit.kilocalories_per_mole))

