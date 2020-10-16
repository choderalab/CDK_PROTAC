from netCDF4 import Dataset
import mdtraj as md
from simtk.openmm.app import PDBFile

pdb = PDBFile('../03123_long0/03123_CDK6_holo_equi.pdb')
topology = md.Topology.from_openmm(pdb.topology)
ref = md.load_pdb('../03123_long0/03123_CDK6_holo_equi.pdb')
solute_ref = ref.remove_solvent()
t = md.load('traj.nc',top=topology)
t = t.image_molecules(anchor_molecules=solute_ref.topology.find_molecules()[0:1], inplace=True)
print("Done imaging molecules.")
short = t[-1]
short.save_pdb('model.pdb')
