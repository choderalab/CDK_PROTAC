import numpy as np

## AMP-PNP
# read in the before radius and calculate volume
before = 0
filename = 'sel_2EUF_amp.sph'
content = open(filename, 'r')
for line in content.readlines():
    line_split = line.strip('\n').split()
    if line_split[0] != 'DOCK' and line_split[0] != 'cluster':
        before += (4/3) * np.pi * (float(line_split[4]) ** 3)

# read in the after radius and calculate volume
after = 0
filename = 'sel_1BI8_amp.sph'
content = open(filename, 'r')
for line in content.readlines():
    line_split = line.strip('\n').split()
    if line_split[0] != 'DOCK' and line_split[0] != 'cluster':
        after += (4/3) * np.pi * (float(line_split[4]) ** 3)

#print('AMP-PNP change: ', round(after - before, 2))
print('AMP-PNP change: ', round(float((after - before)/before), 4))

## palbociclib
# read in the before radius and calculate volume
before = 0
filename = 'sel_2EUF_pal.sph'
content = open(filename, 'r')
for line in content.readlines():
    line_split = line.strip('\n').split()
    if line_split[0] != 'DOCK' and line_split[0] != 'cluster':
        before += (4/3) * np.pi * (float(line_split[4]) ** 3)

# read in the after radius and calculate volume
after = 0
filename = 'sel_1BI8_pal.sph'
content = open(filename, 'r')
for line in content.readlines():
    line_split = line.strip('\n').split()
    if line_split[0] != 'DOCK' and line_split[0] != 'cluster':
        after += (4/3) * np.pi * (float(line_split[4]) ** 3)

#print('palbociclib change: ', round(after - before, 2))
print('palbociclib change: ', round(float((after - before)/before), 4))

