from netCDF4 import Dataset
import mdtraj as md
from simtk.openmm.app import PDBFile
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

pdb = PDBFile('03123_CDK6_holo_equi.pdb')
topology = md.Topology.from_openmm(pdb.topology)
ref = md.load_pdb('03123_CDK6_holo_equi.pdb')
solute_ref = ref.remove_solvent()
t = md.load('traj.nc',top=topology)
t = t.image_molecules(anchor_molecules=solute_ref.topology.find_molecules()[0:1], inplace=True)
print('done imaging molecules')
table, bonds = topology.to_dataframe()
atoms = table.values

# find the atom indices of different proteins in the complex
CDK6 = list()
CRBN = list()
LIG = list()

for i in range(len(atoms)):
    # CDK6
    if atoms[i][5] == 0 and atoms[i][1] in ['C', 'O', 'N', 'CA']:
        CDK6.append(i)
    # CRBN
    if (atoms[i][5] == 3 and atoms[i][1] in ['C', 'O', 'N', 'CA']) or (atoms[i][5] == 4 and atoms[i][1] in ['C', 'O', 'N', 'CA']):
        CRBN.append(i)
    # ligand
    if atoms[i][5] == 5 and atoms[i][4] == 'LIG':
        LIG.append(i)
CDK6_rmsd = md.rmsd(t, t[0], frame=0, atom_indices=np.array(CDK6))
CRBN_rmsd = md.rmsd(t, t[0], frame=0, atom_indices=np.array(CRBN))
LIG_rmsd = md.rmsd(t, t[0], frame=0, atom_indices=np.array(LIG))
# plot the RMSD of different proteins
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec
gs = GridSpec(1, 4)
ax1 = plt.subplot(gs[0, 0:3])
ax2 = plt.subplot(gs[0, 3:], sharey=ax1)
plt.setp(ax2.get_yticklabels(), visible=False)
x_axis = list(range(len(CDK6_rmsd)))
ax1.scatter(x_axis, LIG_rmsd, color='#32cd32', s=5)
ax1.scatter(x_axis, CRBN_rmsd, color='#9DA1E7', s=5)
ax1.scatter(x_axis, CDK6_rmsd, color='#00ced1', s=5, alpha=0.5)
ax2 = sns.distplot(LIG_rmsd, hist=False, kde=True, kde_kws={'shade': True, 'linewidth': 0.5}, vertical=True, color='#32cd32')
ax2 = sns.distplot(CRBN_rmsd, hist=False, kde=True, kde_kws={'shade': True, 'linewidth': 0.5}, vertical=True, color='#9DA1E7')
ax2 = sns.distplot(CDK6_rmsd, hist=False, kde=True, kde_kws={'shade': True, 'linewidth': 0.5}, vertical=True, color='#00ced1')
#ax2.hist(np.array(LIG_rmsd), bins=50, orientation='horizontal', color='#32cd32', linewidth=0.1, align='left', alpha=0.5, edgecolor='black')
#ax2.hist(np.array(CRBN_rmsd), bins=50, orientation='horizontal', color='#9DA1E7', linewidth=0.1, align='left', alpha=0.5, edgecolor='black')
#ax2.hist(np.array(CDK6_rmsd), bins=50, orientation='horizontal', color='#bbedec', linewidth=0.1, align='left', edgecolor='black')
plt.ylim(0.0,3.0)
plt.show()
