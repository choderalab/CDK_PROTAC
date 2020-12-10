import mdtraj as md
import numpy as np
#from math import cos
from simtk.openmm.app import PDBFile
from tqdm import tqdm

# read in the trajectory
pdb = PDBFile('03123_CDK6_holo_equi.pdb')
topology = md.Topology.from_openmm(pdb.topology)
ref = md.load_pdb('03123_CDK6_holo_equi.pdb')
solute_ref = ref.remove_solvent()
t = md.load('traj.nc',top=topology)
t = t.image_molecules(anchor_molecules=solute_ref.topology.find_molecules()[0:1], inplace=True)
print('finish imaging molecules')
equi = 200 # the structure seems stable after this frame
length = len(t)
print(f'length of the simulation: {length}.')

# hard code the residue indices of CDK6 and CRBN (1-based) 
CDK6 = list(range(1,294))
CRBN = list(range(696,1077))
key_inter = dict()
lig_inter = dict()

for i in tqdm(range(length)):
    hbonds = md.baker_hubbard(t[i])
    label = lambda hbond : '%s -- %s' % (t.topology.atom(hbond[0]), t.topology.atom(hbond[2]))
    for hbond in hbonds:
        if (str(t.topology.atom(hbond[0]))[4] == '-' and int(str(t.topology.atom(hbond[0]))[3]) in CDK6) or (str(t.topology.atom(hbond[0]))[5] == '-' and int(str(t.topology.atom(hbond[0]))[3:5]) in CDK6) or (str(t.topology.atom(hbond[0]))[6] == '-' and int(str(t.topology.atom(hbond[0]))[3:6]) in CDK6): # 1-digit CDK6 or 2-digit or 3-digit
            if len(str(t.topology.atom(hbond[2]))) > 7:
                if (str(t.topology.atom(hbond[2]))[6] == '-' and int(str(t.topology.atom(hbond[2]))[3:6]) in CRBN) or (str(t.topology.atom(hbond[2]))[7] == '-' and int(str(t.topology.atom(hbond[2]))[3:7]) in CRBN): # 3-digit CRBN or 4-digit
                    if label(hbond) not in key_inter.keys():
                        key_inter[label(hbond)] = [0] * length # initialize list for one h-bond
                    key_inter[label(hbond)][i] = 1
        if 'LIG' in str(t.topology.atom(hbond[0])) or 'LIG' in str(t.topology.atom(hbond[2])):
            if label(hbond) not in lig_inter.keys():
                lig_inter[label(hbond)] = [0] * length # initialize list for one h-bond
            lig_inter[label(hbond)][i] = 1

# plot the h-bond presence
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec

# set up subplots
ax1=plt.subplot(2, 1, 1)
ax2=plt.subplot(2, 1, 2)
count1 = 1
count2 = 1
print("threshold: ", int((length-equi)/4))
for label in key_inter.keys():
    if sum(key_inter[label][equi+1:]) > int((length-equi)/4):
        ax1.scatter(list(range(equi+2, length+1)), np.array(key_inter[label][equi+1:])*count1, color='#FF4500', s=1.5)
        ax1.text(equi-2.5, count1,str(label),horizontalalignment='right', verticalalignment='center')
        print(count1, label)
        count1 += 1
for label in lig_inter.keys():
    if sum(lig_inter[label][equi+1:]) > int((length-equi)/4):
        ax2.scatter(list(range(equi+2, length+1)), np.array(lig_inter[label][equi+1:])*count2, color='b', s=1.5)
        ax2.text(equi-2.5, count2,str(label),horizontalalignment='right', verticalalignment='center')
        print(count2, label)
        count2 += 1
ax1.set_yticks([])
ax2.set_yticks([])
ax1.set_xlim(equi-10, length+1)
ax2.set_xlim(equi-10, length+1)
ax1.set_xticks([])
plt.show()
del t, key_inter, lig_inter
