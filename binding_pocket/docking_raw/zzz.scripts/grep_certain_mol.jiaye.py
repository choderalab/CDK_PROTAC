#!/usr/bin/env python
# grep molecule of a certain zinc id from a multi-mol2 file

import sys,os

def checkexist(filename):
  if not os.path.isfile(filename):
    print " The file [ %s ] does not exist" % filename
    quit()


inputfilename = str(sys.argv[1])
zinc_list = str(sys.argv[2])
# read in the multimol2 file
checkexist(inputfilename)
inputfile = open(inputfilename, 'r')
lines1 = inputfile.readlines()
inputfile.close()

# read in the name list
checkexist(zinc_list)
names = open(zinc_list)
lines2 = names.readlines()
names.close()

for line2 in lines2:
    line_split2 = line2.split('\n')
    print 'grep molecule:'+str(line_split2[0])
    count = 0
    for line1 in lines1:
        if (count == 0) and (str(line_split2[0]) in line1):
            count = 1
            name = str(line_split2[0]) + '.mol2'
            outfile = file(str(name), 'w')
            a = line1
            outfile.write(a)
        else:
            if (count > 0) and ('Name_DOCK:' not in line1) and ('ROOT' not in line1):
                b = line1
                outfile.write(b)
            elif (count > 0) and ('ROOT' in line1):
                c = line1
                outfile.write(c)
                outfile.close()
                break
