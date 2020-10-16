#!/usr/bin/python

import sys
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

### This script plots footprint generated from DOCK. 
### Usage: python plot_dock_clean.py [footprint.txt] max_res
####################################################################################################

def identify_residues(filename, max_res):

    ### Read in the footprint file
    footprint = open(filename,'r')
    lines = footprint.readlines()
    footprint.close()

    ### Count the number of residues in footprint.txt file
    num_res = 0
    for line in lines:
        linesplit = line.split()
        if (len(linesplit) == 8):
            if (linesplit[0] != 'resname'):
                num_res += 1
    k = 0
    fp_array = [[0 for i in range(2)] for j in range(num_res)]
    for line in lines:
        linesplit = line.split()
        if (len(linesplit) == 8):
            if (linesplit[0] != 'resname'):
                k += 1
                fp_array[k-1][0] = k
                fp_array[k-1][1] = max(math.fabs(float(linesplit[2])), math.fabs(float(linesplit[3])), math.fabs(float(linesplit[5])), math.fabs(float(linesplit[6])))

    fp_array.sort(key=lambda x: x[1])
    resindex_selected = []
    resindex_remainder = []
    
    for i in range(max_res):
        resindex_selected.append(int(fp_array[(num_res-1)-i][0]))

    for i in range(num_res - max_res):
        resindex_remainder.append(int(fp_array[i][0]))

    resindex_selected.sort()
    resindex_remainder.sort()
    return resindex_selected, resindex_remainder

####################################################################################################

def plot_footprints(filename, resindex_selected, resindex_remainder):

    footprint = open(filename,'r')
    lines = footprint.readlines()
    footprint.close()

    ### Store the resname, resid, and fp information appropriately
    resname = []; resid = []; vdw_ref = []; es_ref = []; vdw_pose = []; es_pose = []
    vdw_score = ""; es_score = ""
    vdw_energy = ""; es_energy = ""

    for line in lines:
        linesplit = line.split()
        if (len(linesplit) == 3):
            if (linesplit[1] == 'vdw_fp:'):
                vdw_score = 'd = '+linesplit[2]
            if (linesplit[1] ==  'es_fp:'):
                es_score = 'd = '+linesplit[2]
            if (linesplit[1] == 'vdw:'):
                vdw_energy = 'vdw = '+linesplit[2]+' kcal/mol'
            if (linesplit[1] == 'es:'):
                es_energy = 'es = '+linesplit[2]+' kcal/mol'
        if (len(linesplit) == 8):
            if (linesplit[0] != 'resname'):
                resname.append(linesplit[0]+str(linesplit[1]))
                resid.append(int(linesplit[1]))
                vdw_ref.append(float(linesplit[2]))
                es_ref.append(float(linesplit[3]))
                vdw_pose.append(float(linesplit[5]))
                es_pose.append(float(linesplit[6]))

    ### Put the selected residues onto a selected array
    resname_selected = []
    vdw_ref_selected = []; es_ref_selected = []; vdw_pose_selected = []; es_pose_selected = []

    for i in (resindex_selected):
        resname_selected.append(resname[i-1])
        vdw_ref_selected.append(vdw_ref[i-1])
        es_ref_selected.append(es_ref[i-1])
        vdw_pose_selected.append(vdw_pose[i-1])
        es_pose_selected.append(es_pose[i-1])

    ### Compute the sums for the remainder residues
    vdw_ref_remainder = 0; es_ref_remainder = 0; vdw_pose_remainder = 0; es_pose_remainder = 0

    for i in (resindex_remainder):
        vdw_ref_remainder += vdw_ref[i-1]
        es_ref_remainder += es_ref[i-1]
        vdw_pose_remainder += vdw_pose[i-1]
        es_pose_remainder += es_pose[i-1]

    ### Append the remainders to the end of the selected arrays
    resname_selected.append('REMAIN')
    vdw_ref_selected.append(vdw_ref_remainder)
    es_ref_selected.append(es_ref_remainder)
    vdw_pose_selected.append(vdw_pose_remainder)
    es_pose_selected.append(es_pose_remainder)
        
    ### Create an index for plotting
    residue = []
        
    for i in range(len(resname_selected)):
        residue.append(i)

    ### Check for self consistency
    #print (sum(vdw_pose_selected) - sum(vdw_pose)) + (sum(vdw_ref_selected) - sum(vdw_ref)) + (sum(es_pose_selected) - sum(es_pose)) + (sum(es_ref_selected) - sum(es_ref))

    ### Plot the figure
    fig = plt.figure(figsize=(12, 11))
    ax1 = fig.add_subplot(2,1,1)
    ax1.set_title('HER2 Bridging Water')
    plt.plot(residue, vdw_ref_selected, 'm', linewidth=3)
    plt.plot(residue, vdw_pose_selected, 'm', linewidth=3)
    ax1.set_ylabel('VDW Energy')
    ax1.set_ylim(-6, 3)
    ax1.set_xlim(0, len(resname_selected))
    ax1.xaxis.set_major_locator(MultipleLocator(1))
    ax1.xaxis.set_major_formatter(FormatStrFormatter('%s'))
    ax1.set_xticks(residue)
    ax1.xaxis.grid(which='major', color='black', linestyle='solid')
    ax1.set_xticklabels(resname_selected, rotation=90)
    ax1.legend(['Ligand + Water'], 'upper left')
    ax1.annotate(vdw_score, xy=(5,-4), backgroundcolor='white', bbox={'facecolor':'white', 'alpha':1.0, 'pad':10})
    ax1.annotate(vdw_energy, xy=(5,-5), backgroundcolor='white', bbox={'facecolor':'white', 'alpha':1.0, 'pad':10})
    ax1.axhline(y=0,color='k',ls='dashed')       
 
    ax2 = fig.add_subplot(2,1,2)
    plt.plot(residue, es_ref_selected, 'm', linewidth=3)
    plt.plot(residue, es_pose_selected, 'm', linewidth=3)
    ax2.set_ylabel('ES Energy')
    ax2.set_ylim(-6, 3)
    ax2.set_xlim(0, len(resname_selected))
    ax2.xaxis.set_major_locator(MultipleLocator(1))
    ax2.xaxis.set_major_formatter(FormatStrFormatter('%s'))
    ax2.set_xticks(residue)
    ax2.xaxis.grid(which='major', color='black', linestyle='solid')
    ax2.set_xticklabels(resname_selected, rotation=90)
    ax2.legend()
    ax2.annotate(es_score, xy=(5,-8), backgroundcolor='white', bbox={'facecolor':'white', 'alpha':1.0, 'pad':10})
    ax2.annotate(es_energy, xy=(5,-10), backgroundcolor='white', bbox={'facecolor':'white', 'alpha':1.0, 'pad':10})
    ax2.axhline(y=0,color='k',ls='dashed')
    ### If you want to save the footprint in pdf.   
    #plt.savefig('ref-footprint'+'.pdf')
    plt.show()
    plt.close()

    del resname[:]
    del resid[:]
    del vdw_ref[:]
    del es_ref[:]
    del vdw_pose[:]
    del es_pose[:]
    del resname_selected[:]
    del vdw_ref_selected[:]
    del es_ref_selected[:]
    del vdw_pose_selected[:]
    del es_pose_selected[:]
    del residue[:]

    return

####################################################################################################

def main():

    ### Get the command line arguments
    filename = sys.argv[1]
    max_res = int(sys.argv[2])

    ### Go through the first time to identify interactions above the threshold
    (resindex_selected, resindex_remainder) = identify_residues(filename, max_res)

    #print resindex_selected; print "\n"; print resindex_remainder
    #print "\n"; print len(resindex_selected); print len(resindex_remainder)

    ### Go through a second time to write plots to file
    plot_footprints(filename, resindex_selected, resindex_remainder)


    return

####################################################################################################

main()

