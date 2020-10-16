#! /usr/bin/python

import math
import sys

## THIS CODE WAS WRITEN BY TRENT E BALIUS
## STONY BROOK UNIVERSITY
## STARTED 2010-02-27

class parm:
     def __init__(self,RESIDUE_POINTER,RESIDUE_LABEL, RESIDUE_ARRAY, ATOM_NAME, AMBER_ATOM_TYPE, ATOM_TYPE_INDEX, CHARGE,MASS, M_LJA, M_LJB):
         # NOTE THIS IS NOT COMPLET YET.
         # WE SHOULD ADD IN ALL COMPONENTS REPRESENTED IN A PARM FILE
         self.RESIDUE_POINTER = RESIDUE_POINTER
         self.RESIDUE_LABEL = RESIDUE_LABEL
         self.RESIDUE_ARRAY   = RESIDUE_ARRAY   # vector of N (number of atoms) elements
         self.ATOM_NAME       = ATOM_NAME       # vector of N
         self.AMBER_ATOM_TYPE = AMBER_ATOM_TYPE # vector of N
         self.ATOM_TYPE_INDEX = ATOM_TYPE_INDEX # vector of N
         self.CHARGE          = CHARGE          # vector of N
         self.MASS            = MASS            # vector of N
         self.M_LJA           = M_LJA           # MxM matrix where M is the number of amber atom types
                                                # in the system
         self.M_LJB           = M_LJB           # MxM matrix 

class cord:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class frame:
    def __init__(self, cords):
        self.cords = cords ## list of coordenates 



## read in parm file
def parm_reader(filename):
 file = open(filename,'r')
##%VERSION  VERSION_STAMP = V0001.000  DATE = 07/09/07  12:35:37                  
 TITLE                      = []   
 POINTERS                   = []   
 ATOM_NAME                  = []  
 CHARGE                     = []  
 MASS                       = [] 
 ATOM_TYPE_INDEX            = [] 
 NUMBER_EXCLUDED_ATOMS      = []  
 NONBONDED_PARM_INDEX       = []  
 RESIDUE_LABEL              = []  
 RESIDUE_POINTER            = []  
 BOND_FORCE_CONSTANT        = []  
 BOND_EQUIL_VALUE           = []  
 ANGLE_FORCE_CONSTANT       = []  
 ANGLE_EQUIL_VALUE          = []  
 DIHEDRAL_FORCE_CONSTANT    = []  
 DIHEDRAL_PERIODICITY       = []  
 DIHEDRAL_PHASE             = []  
 SOLTY                      = []  
 LENNARD_JONES_ACOEF        = []  
 LENNARD_JONES_BCOEF        = []  
 BONDS_INC_HYDROGEN         = []  
 BONDS_WITHOUT_HYDROGEN     = []  
 ANGLES_INC_HYDROGEN        = []  
 ANGLES_WITHOUT_HYDROGEN    = []  
 DIHEDRALS_INC_HYDROGEN     = []  
 DIHEDRALS_WITHOUT_HYDROGEN = []  
 EXCLUDED_ATOMS_LIST        = []  
 HBOND_ACOEF                = []  
 HBOND_BCOEF                = []  
 HBCUT                      = []  
 AMBER_ATOM_TYPE            = []  
 TREE_CHAIN_CLASSIFICATION  = []  
 JOIN_ARRAY                 = []  
 IROTAT                     = []  
 RADII                      = []  
 SCREEN                     = []  


 ## INSHALIZE FLAGS
 F_TITLE                      = False
 F_POINTERS                   = False
 F_ATOM_NAME                  = False
 F_CHARGE                     = False
 F_MASS                       = False
 F_ATOM_TYPE_INDEX            = False
 F_NUMBER_EXCLUDED_ATOMS      = False
 F_NONBONDED_PARM_INDEX       = False
 F_RESIDUE_LABEL              = False
 F_RESIDUE_POINTER            = False 
 F_BOND_FORCE_CONSTANT        = False
 F_BOND_EQUIL_VALUE           = False
 F_ANGLE_FORCE_CONSTANT       = False
 F_ANGLE_EQUIL_VALUE          = False
 F_DIHEDRAL_FORCE_CONSTANT    = False
 F_DIHEDRAL_PERIODICITY       = False
 F_DIHEDRAL_PHASE             = False
 F_SOLTY                      = False
 F_LENNARD_JONES_ACOEF        = False
 F_LENNARD_JONES_BCOEF        = False
 F_BONDS_INC_HYDROGEN         = False
 F_BONDS_WITHOUT_HYDROGEN     = False
 F_ANGLES_INC_HYDROGEN        = False
 F_ANGLES_WITHOUT_HYDROGEN    = False
 F_DIHEDRALS_INC_HYDROGEN     = False
 F_DIHEDRALS_WITHOUT_HYDROGEN = False
 F_EXCLUDED_ATOMS_LIST        = False
 F_HBOND_ACOEF                = False
 F_HBOND_BCOEF                = False
 F_HBCUT                      = False
 F_AMBER_ATOM_TYPE            = False
 F_TREE_CHAIN_CLASSIFICATION  = False
 F_JOIN_ARRAY                 = False
 F_IROTAT                     = False
 F_RADII                      = False
 F_SCREEN                     = False


 for line in file:
  split_line = line.split()
  if len(split_line) >= 1: #UPDATE 11-13-2011: Allows for lines with one data point on them
   if (split_line[0] == "%FLAG"):  ## EVERY TIME A NEW FLAG IS SEEN REINSHALIZE ALL FLAGS 
      F_TITLE                      = False
      F_POINTERS                   = False
      F_ATOM_NAME                  = False
      F_CHARGE                     = False
      F_MASS                       = False
      F_ATOM_TYPE_INDEX            = False
      F_NUMBER_EXCLUDED_ATOMS      = False
      F_NONBONDED_PARM_INDEX       = False
      F_RESIDUE_LABEL              = False
      F_RESIDUE_POINTER            = False 
      F_BOND_FORCE_CONSTANT        = False
      F_BOND_EQUIL_VALUE           = False
      F_ANGLE_FORCE_CONSTANT       = False
      F_ANGLE_EQUIL_VALUE          = False
      F_DIHEDRAL_FORCE_CONSTANT    = False
      F_DIHEDRAL_PERIODICITY       = False
      F_DIHEDRAL_PHASE             = False
      F_SOLTY                      = False
      F_LENNARD_JONES_ACOEF        = False
      F_LENNARD_JONES_BCOEF        = False
      F_BONDS_INC_HYDROGEN         = False
      F_BONDS_WITHOUT_HYDROGEN     = False
      F_ANGLES_INC_HYDROGEN        = False
      F_ANGLES_WITHOUT_HYDROGEN    = False
      F_DIHEDRALS_INC_HYDROGEN     = False
      F_DIHEDRALS_WITHOUT_HYDROGEN = False
      F_EXCLUDED_ATOMS_LIST        = False
      F_HBOND_ACOEF                = False
      F_HBOND_BCOEF                = False
      F_HBCUT                      = False
      F_AMBER_ATOM_TYPE            = False
      F_TREE_CHAIN_CLASSIFICATION  = False
      F_JOIN_ARRAY                 = False
      F_IROTAT                     = False
      F_RADII                      = False
      F_SCREEN                     = False

   if ((split_line[0] == "%FLAG") and  (split_line[1]=="TITLE")):
      F_TITLE                      = True 
      
   if ((split_line[0] == "%FLAG") and (split_line[1]=="POINTERS")):                                       
      F_POINTERS                   = True
      
   if ((split_line[0] == "%FLAG") and (split_line[1]== "ATOM_NAME")):
      F_ATOM_NAME                  = True
      
   if ((split_line[0] == "%FLAG") and (split_line[1]==  "CHARGE")):
      F_CHARGE                     = True 

   if ((split_line[0] == "%FLAG") and (split_line[1] == "MASS")):
      F_MASS                       = True

   ## ATOM_TYPE_INDEX IS ALSO CALLED IAC (see http://ambermd.org/formats.html)
   if ((split_line[0] == "%FLAG") and (split_line[1] == "ATOM_TYPE_INDEX")):
      F_ATOM_TYPE_INDEX            = True


   if ((split_line[0] == "%FLAG") and (split_line[1] == "NUMBER_EXCLUDED_ATOMS")):
      F_NUMBER_EXCLUDED_ATOMS      = True

# see http://ambermd.org/formats.html
#%FLAG NUMBER_EXCLUDED_ATOMS
#%FORMAT(10I8)  (NUMEX(i), i=1,NATOM)
#  NUMEX  : total number of excluded atoms for atom "i".  Also called IBLO. See
#           NATEX below.



   if ((split_line[0] == "%FLAG") and (split_line[1] == "NONBONDED_PARM_INDEX")):
      F_NONBONDED_PARM_INDEX       = True

   ## NONBONDED_PARM_INDEX IS ALSO CALLED ICO (see http://ambermd.org/formats.html)
   ## NOTE THE FOLLOWING COPYED FROM http://ambermd.org/formats.html

   #%FORMAT(10I8)  (ICO(i), i=1,NTYPES*NTYPES)
   #  ICO    : provides the index to the nonbon parameter
   #           arrays CN1, CN2 and ASOL, BSOL.  All possible 6-12
   #           or 10-12 atoms type interactions are represented.
   #           NOTE: A particular atom type can have either a 10-12
   #           or a 6-12 interaction, but not both.  The index is
   #           calculated as follows:
   #             index = ICO(NTYPES*(IAC(i)-1)+IAC(j))
   #           If index is positive, this is an index into the
   #           6-12 parameter arrays (CN1 and CN2) otherwise it
   #           is an index into the 10-12 parameter arrays (ASOL
   #           and BSOL).

   #            index = ICO(NTYPES*(i)+j)
   #            i = 0, j = 0 => NTYPES*(i)+j = 0
   #            i = 0, j = k => NTYPES*(i)+j = k
   #            and so on.
   #            this maps a NxN matrix to a N^2 vector.
   #            for some reason, they choses to do this for the 
   #            index rather than for the actual float values.

   if ((split_line[0] == "%FLAG") and (split_line[1] == "RESIDUE_LABEL")):
      F_RESIDUE_LABEL              = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "RESIDUE_POINTER")):
      F_RESIDUE_POINTER            = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "BOND_FORCE_CONSTANT")): 
      F_BOND_FORCE_CONSTANT        = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "BOND_EQUIL_VALUE")): 
      F_BOND_EQUIL_VALUE           = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "ANGLE_FORCE_CONSTANT")):
      F_ANGLE_FORCE_CONSTANT       = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "ANGLE_EQUIL_VALUE")):
      F_ANGLE_EQUIL_VALUE          = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "DIHEDRAL_FORCE_CONSTANT")):
      F_DIHEDRAL_FORCE_CONSTANT    = True 

   if ((split_line[0] == "%FLAG") and (split_line[1] == "DIHEDRAL_PERIODICITY")):
      F_DIHEDRAL_PERIODICITY       = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "DIHEDRAL_PHASE")):
      F_DIHEDRAL_PHASE             = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "SOLTY")):
      F_SOLTY                      = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "LENNARD_JONES_ACOEF")):
      F_LENNARD_JONES_ACOEF        = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "LENNARD_JONES_BCOEF")):
      F_LENNARD_JONES_BCOEF        = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "BONDS_INC_HYDROGEN")):
      F_BONDS_INC_HYDROGEN         = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "BONDS_WITHOUT_HYDROGEN")):
      F_BONDS_WITHOUT_HYDROGEN     = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "ANGLES_INC_HYDROGEN")):
      F_ANGLES_INC_HYDROGEN        = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "ANGLES_WITHOUT_HYDROGEN")):
      F_ANGLES_WITHOUT_HYDROGEN    = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "DIHEDRALS_INC_HYDROGEN")):
      F_DIHEDRALS_INC_HYDROGEN     = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "DIHEDRALS_WITHOUT_HYDROGEN")):
      F_DIHEDRALS_WITHOUT_HYDROGEN = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "EXCLUDED_ATOMS_LIST")):
      F_EXCLUDED_ATOMS_LIST        = True

# see http://ambermd.org/formats.html
# %FLAG EXCLUDED_ATOMS_LIST
# %FORMAT(10I8)  (INB(i), i=1,NNB)
#   INB    : the excluded atom list.  To get the excluded list for atom 
#            "i" you need to traverse the NUMEX list, adding up all
#            the previous NUMEX values, since NUMEX(i) holds the number
#            of excluded atoms for atom "i", not the index into the 
#            NATEX list.  Let IEXCL = SUM(NUMEX(j), j=1,i-1), then
#            excluded atoms are INB(IEXCL) to INB(IEXCL+NUMEX(i)). Note,
#            this array was called NATEX at one point, and while in most
#            places it is now INB, it is still called NATEX in some places
#            (especially in pmemd)

   if ((split_line[0] == "%FLAG") and (split_line[1] == "HBOND_ACOEF")):
      F_HBOND_ACOEF                = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "HBOND_BCOEF")):
      F_HBOND_BCOEF                = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "HBCUT")):
      F_HBCUT                      = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "AMBER_ATOM_TYPE")):
      F_AMBER_ATOM_TYPE            = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "TREE_CHAIN_CLASSIFICATION")):
      F_TREE_CHAIN_CLASSIFICATION  = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "JOIN_ARRAY")):  
      F_JOIN_ARRAY                 = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "IROTAT")):
      F_IROTAT                     = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "RADII")):
      F_RADII                      = True

   if ((split_line[0] == "%FLAG") and (split_line[1] == "SCREEN")):
      F_SCREEN                     = True

#  if ( F_TITLE                      ): 
#      print "F_TITLE"

   ## READ IN THE NUMBER OF ELEMENTS FOR 
   ## AS WELL AS FLAGS.
   if ( F_POINTERS                   ):
     if not(line[0] == "%"):
       i = 0
       line = line.strip('\n')
       while i < len(line):
          temp_POINTERS = line[i:i+8].replace(' ', '')
          POINTERS.append(int(temp_POINTERS))
          i = i + 8
    
   if ( F_ATOM_NAME                  ):
     if not(line[0] == "%"):
       i = 0
       line = line.strip('\n')
       while i < len(line):
          ATOM_NAME.append(line[i:i+4])
          i = i + 4 
 
   if ( F_CHARGE                     ):
     if not(line[0] == "%"):
       i = 0
       line = line.strip('\n')
       while i < len(line):
          temp_CHARGE = line[i:i+16].replace(' ', '')
          CHARGE.append(float(temp_CHARGE))
          i = i + 16
 
   if ( F_MASS                       ):
     if not(line[0] == "%"):
       i = 0
       line = line.strip('\n')
       while i < len(line):
          temp_MASS = line[i:i+16].replace(' ', '')
          MASS.append(float(temp_MASS))
          i = i + 16

   if ( F_ATOM_TYPE_INDEX            ):
     if not(line[0] == "%"):
       i = 0
       line = line.strip('\n')
       while i < len(line):
          temp_ATOM_TYPE_INDEX = line[i:i+8].replace(' ', '')
          ATOM_TYPE_INDEX.append(int(temp_ATOM_TYPE_INDEX))
          i = i + 8

#  if ( F_NUMBER_EXCLUDED_ATOMS      ):
#       print "F_NUMBER_EXCLUDED_ATOMS" 

   if ( F_NONBONDED_PARM_INDEX       ):
     if not(line[0] == "%"):
       i = 0
       line = line.strip('\n')
       while i < len(line):
          temp_NONBONDED_PARM_INDEX = line[i:i+8].replace(' ', '')
          NONBONDED_PARM_INDEX.append(int(temp_NONBONDED_PARM_INDEX))
          i = i + 8
 
   if ( F_RESIDUE_LABEL              ):
     if not(line[0] == "%"):
       i = 0
       line = line.strip('\n')
       while i < len(line):
          RESIDUE_LABEL.append(line[i:i+4])
          i = i + 4
   if ( F_RESIDUE_POINTER            ):
     if not(line[0] == "%"):
       i = 0
       line = line.strip('\n')
       while i < len(line):
          temp_RESIDUE_POINTER = line[i:i+8].replace(' ', '')
          RESIDUE_POINTER.append(int(temp_RESIDUE_POINTER))
          i = i + 8
  
#  if ( F_BOND_FORCE_CONSTANT        ):
#       print "F_BOND_FORCE_CONSTANT" 
#  if ( F_BOND_EQUIL_VALUE           ):
#       print "F_BOND_EQUIL_VALUE" 
#  if ( F_ANGLE_FORCE_CONSTANT       ): 
#       print "F_ANGLE_FORCE_CONSTANT"
#  if ( F_ANGLE_EQUIL_VALUE          ):
#       print "F_ANGLE_EQUIL_VALUE" 
#  if ( F_DIHEDRAL_FORCE_CONSTANT    ): 
#       print "F_DIHEDRAL_FORCE_CONSTANT"
#  if ( F_DIHEDRAL_PERIODICITY       ): 
#       print "F_DIHEDRAL_PERIODICITY"
#  if ( F_DIHEDRAL_PHASE             ):
#       print "F_DIHEDRAL_PHASE" 
#  if ( F_SOLTY                      ):
#       print "F_SOLTY"
 
   if ( F_LENNARD_JONES_ACOEF        ): 
      if not(line[0] == "%"):
       i = 0
       line = line.strip('\n')
       while i < len(line):
          temp_LENNARD_JONES_ACOEF = line[i:i+16].replace(' ', '')
          LENNARD_JONES_ACOEF.append(float(temp_LENNARD_JONES_ACOEF))
          i = i + 16

 
   if ( F_LENNARD_JONES_BCOEF        ): 
      if not(line[0] == "%"):
       i = 0
       line = line.strip('\n')
       while i < len(line):
          temp_LENNARD_JONES_BCOEF = line[i:i+16].replace(' ', '')
          LENNARD_JONES_BCOEF.append(float(temp_LENNARD_JONES_BCOEF))
          i = i + 16

#  if ( F_BONDS_INC_HYDROGEN         ): 
#       print "F_BONDS_INC_HYDROGEN" 
#  if ( F_BONDS_WITHOUT_HYDROGEN     ): 
#       print "F_BONDS_WITHOUT_HYDROGEN" 
#  if ( F_ANGLES_INC_HYDROGEN        ): 
#       print "F_ANGLES_INC_HYDROGEN" 
#  if ( F_ANGLES_WITHOUT_HYDROGEN    ): 
#       print "F_ANGLES_WITHOUT_HYDROGEN" 
#  if ( F_DIHEDRALS_INC_HYDROGEN     ): 
#       print "F_DIHEDRALS_INC_HYDROGEN" 
#  if ( F_DIHEDRALS_WITHOUT_HYDROGEN ):
#       print "F_DIHEDRALS_WITHOUT_HYDROGEN" 
#  if ( F_EXCLUDED_ATOMS_LIST        ):  
#       print "F_EXCLUDED_ATOMS_LIST" 
#  if ( F_HBOND_ACOEF                ): 
#       print "F_HBOND_ACOEF" 
#  if ( F_HBOND_BCOEF                ): 
#       print "F_HBOND_BCOEF" 
#  if ( F_HBCUT                      ): 
#       print "F_HBCUT" 

   if ( F_AMBER_ATOM_TYPE            ): 
     if not(line[0] == "%"):
       i = 0
       line = line.strip('\n')
       while i < len(line):
          AMBER_ATOM_TYPE.append(line[i:i+4])
          i = i + 4
 
#  if ( F_TREE_CHAIN_CLASSIFICATION  ): 
#       print "F_TREE_CHAIN_CLASSIFICATION" 
#  if ( F_JOIN_ARRAY                 ): 
#       print "F_JOIN_ARRAY" 
#  if ( F_IROTAT                     ): 
#       print "F_IROTAT" 
#  if ( F_RADII                      ): 
#       print "F_RADII" 
#  if ( F_SCREEN                     ): 
#       print "F_SCREEN" 

# print str(len(ATOM_NAME)) + " " + str(len(ATOM_TYPE_INDEX)) 

 ## find what atoms go with what residues 

 RESIDUE_ARRAY = []

 ##INISHALIZE A EMPTY ARRAY
 for i in range(len(ATOM_NAME)):
     RESIDUE_ARRAY.append("");

 ## FILL IN THE RESIDUE NAMES:

 for i in range(0,len(RESIDUE_POINTER)-1):
     for j in range(RESIDUE_POINTER[i],(RESIDUE_POINTER[i+1])):
          RESIDUE_ARRAY[j-1] = RESIDUE_LABEL[i]

    ## for last residue
 for j in range(RESIDUE_POINTER[len(RESIDUE_POINTER)-1]-1,len(ATOM_NAME)):
     #print j
     RESIDUE_ARRAY[j] = RESIDUE_LABEL[len(RESIDUE_LABEL)-1]



 ## count the number of atoms of certien types. 

 print "ATOM_NAME = ",len(ATOM_NAME)
 print "CHARGE = ",len(CHARGE)
 print "MASS   = ",len(MASS)
 print "ATOM_TYPE_INDEX = ",len(ATOM_TYPE_INDEX)
 print "max(ATOM_TYPE_INDEX) =", max(ATOM_TYPE_INDEX) 
 print "max(ATOM_TYPE_INDEX)^2 =", max(ATOM_TYPE_INDEX)*max(ATOM_TYPE_INDEX)
 print "NONBONDED_PARM_INDEX = ",len(NONBONDED_PARM_INDEX)
 print "max(NONBONDED_PARM_INDEX) = ",max(NONBONDED_PARM_INDEX)
 print "LENNARD_JONES_ACOEF = ",len(LENNARD_JONES_ACOEF)
 print "LENNARD_JONES_BCOEF = ",len(LENNARD_JONES_BCOEF)

#for i in range(len(ATOM_NAME)):
#   print RESIDUE_ARRAY[i] + "  " + str(i)+ " " + ATOM_NAME[i] + " " + AMBER_ATOM_TYPE[i] + " " + str(ATOM_TYPE_INDEX[i]) + " " + str(CHARGE[i]) 

 atom_type_uniq = []


 for AtomNum in range(1,max(ATOM_TYPE_INDEX)+1):
    count = 0
    for i in range(len(ATOM_TYPE_INDEX)):
        if AtomNum == ATOM_TYPE_INDEX[i]:
           if (count == 0):
               atom_type_uniq.append(AMBER_ATOM_TYPE[i]) 
           count = count+1
   #print "ATOM_TYPE_INDEX == " + str(AtomNum) + " has N = " + str(count) + " atoms of this type"
 
 ## play with LJ matrixes, see how it is orginized?  I did not understand the 
 #%FLAG LENNARD_JONES_ACOEF
 #%FORMAT(5E16.8)  (CN1(i), i=1,NTYPES*(NTYPES+1)/2)
 #  CN1  : Lennard Jones r**12 terms for all possible atom type interactions,
 #         indexed by ICO and IAC; for atom i and j where i < j, the index into
 #         this array is as follows (assuming the value of ICO(index) is positive):
 #         CN1(ICO(NTYPES*(IAC(i)-1)+IAC(j))).
 ## web page explination at : http://ambermd.org/formats.html
 #print "\n\n LJ matrixes"

 ## make matrix 

 M_index = []
 M_LJA = []
 M_LJB = []

 for i in range(0,max(ATOM_TYPE_INDEX)):
     rowi = []
     rowA = []
     rowB = []
     for j in range(0,max(ATOM_TYPE_INDEX)):
         rowi.append(0.0)
         rowA.append(0.0)
         rowB.append(0.0)
     M_index.append(rowi)
     M_LJA.append(rowA)
     M_LJB.append(rowB)
#HOLDEN: Need discussion of how this works
 NTYPES = POINTERS[1]
 for i in range(0,(NTYPES)):
    for j in range(0,(NTYPES)):
        index = NONBONDED_PARM_INDEX[(NTYPES)*(i)+j]
        #print i,j,(NTYPES)*(i)+j,index, LENNARD_JONES_ACOEF[index-1] 
        M_index[i][j] = index-1
        M_LJA[i][j]   = LENNARD_JONES_ACOEF[index-1]
        M_LJB[i][j]   = LENNARD_JONES_BCOEF[index-1]

#print "index:"
#print_matrix_d(M_index)
#print "LENNARD_JONES_ACOEF:"
#print_matrix(M_LJA)
#print "LENNARD_JONES_BCOEF:"
#print_matrix(M_LJB)

 # see Molecular Modelling prenciples and approches by Leach p. 207
 # ACOEF = eps*rm^12 and BCOEF = 2*eps*rm^6 
#print "AMBER ATOM TYPE, ACOEF, BCOEF "
#for i in range(0,len(atom_type_uniq)):
#   print atom_type_uniq[i],M_LJA[i][i], M_LJB[i][i]

# print "\n test LJ mat is right" 
#
# print M_LJA[1][1], M_LJA[2][2]
# print M_LJA[1][1] * M_LJA[2][2]
# 
#
# temp_12 = math.sqrt( M_LJA[1][1] * M_LJA[2][2] )
# print M_LJA[2][1], temp_12
#
#
 parm_stuff = parm(RESIDUE_POINTER, RESIDUE_LABEL, RESIDUE_ARRAY, ATOM_NAME, AMBER_ATOM_TYPE, ATOM_TYPE_INDEX, CHARGE,MASS, M_LJA, M_LJB)
 return parm_stuff
def print_matrix(M):
 for i in range(0,len(M)):
     for j in range(0,len(M[i])):
        print "%10.1f" % M[i][j],
     print ""

 return

def print_matrix_d(M):
 for i in range(0,len(M)):
     for j in range(0,len(M[i])):
        print "%4d" % M[i][j],
     print ""

 return

def cord_reader(filename,size):
 
 print "IN cord_reader"
 file = open(filename,'r')
# lines = file.readlines()

 frames = []
 cords  = []
 count  = 0 
 line_count = 0 
 rdparm_flag = False
 reset_flag = True
 in_frame = False
 temp_raw_crds = []

 print "size = " + str(size)
# for line in lines:
 for line in file:
   data = line.strip('\n').split(' ')

   if ( line_count == 0 ) and ( len(data) > 0): #Note: This is the header for ptraj transformed trajectory #JIAYE(07-06-15): for rst files minimized with AMBER12, when line_count ==0, len(data) is also 0!
       if (data[0] == 'rdparm') or (data[0] == 'ptraj') or (data[0] == 'Cpptraj'): #HOLDEN: Addtion 11-13-2011 - MUST CHECK EDITION OF PTRAJ!!!
           rdparm_flag = True
           print "This is a ptraj modified trajectory."

   if rdparm_flag:  #rdparm trajectories have 10 coordinates per line; cat 3 lines together, then get coordinates
     if line_count > 0:  #Gets rid of header line
       ls = line.strip('\n').split()
       if not in_frame and len(ls) == 10: #Box info might be between frames; this gets rid of it
         in_frame = True
       if reset_flag and in_frame:  #Determines if at start of new set of 10 coordinates
         if count <= (size - 7): #If next three lines must be concantenated; middle set of 10 or last 7-10 coordinates
            j = 0
         elif count <= (size - 4): #If next two lines concat; i.e. last 4-6 residues
            j = 1
         else:
            j = 2  #If need just last line alone; i.e. last 1-3 resdiues
         reset_flag = False #Indicates in a set of coordinates
       if not reset_flag and in_frame:
         if (j == 0) or (j == 1):
           temp_raw_crds = temp_raw_crds + ls
           j = j + 1
         elif ( j == 2 ):
#          print "j = " + str(j)
           temp_raw_crds = temp_raw_crds + ls
#          print temp_raw_crds
           i = 0
           while i < len(temp_raw_crds):
              x = float(temp_raw_crds[i])
              y = float(temp_raw_crds[i+1])
              z = float(temp_raw_crds[i+2])
              temp_cord = cord(x,y,z)
#             print_crd(temp_cord)
              cords.append(temp_cord)
              i = i + 3
              count = count + 1
           if count == size: #i.e. end of frame
              temp_frame = frame(cords)
              frames.append(temp_frame)
              cords  = []
              count  = 0
              in_frame = False
#             print "Frames = " + str(len(frames))
           reset_flag = True
           temp_raw_crds = []
 
        

   else: #From trajectories from SANDER
     if line_count == 1:
        if len(data) == 1: 
           if size != int(data[0]): #HOLDEN: compares reported number of atoms in crd with residue_array; 11-13-11
             print "Number of atoms in trajectory does not match parm file.  Exiting."
             sys.exit(0)
	else:
           print "unfamiliar format"
     if line_count > 1:
       i = 0
       while i < len(data):
          if count == size:
             temp_frame = frame(cords)
             frames.append(temp_frame)
             cords  = []
             count  = 0
          x = float(data[i])
          y = float(data[i+1])
          z = float(data[i+2])
          temp_cord = cord(x,y,z)
          cords.append(temp_cord)
          i = i + 3
          count = count + 1
   line_count = line_count + 1
 file.close()
 if not rdparm_flag:
   temp_frame = frame(cords)
   frames.append(temp_frame)
 #print_frame(frames)
 #print frames
 return frames 

def print_frame(frames):
  for i in range(len(frames)):
    print "This is frame number " +str(i) + "."
    for j in range(len(frames[i].cords)):
      print str(frames[i].cords[j].x) + "," + str(frames[i].cords[j].y) + "," + str(frames[i].cords[j].z) 

def print_crd(crd):
   print str(crd.x) + "," + str(crd.y) + "," + str(crd.z) 

def distance(crd1,crd2):
    r = ((crd1.x - crd2.x)**2.0 + (crd1.y - crd2.y)**2.0 + ( crd1.z - crd2.z)**2.0)**(0.5)
    #print crd1.x,crd2.x,crd1.y,crd2.y,crd1.z,crd2.z,r
    return r

def vdw_energy_function(A,B,r):
    return A/(r**12) - B/(r**6)

def es_energy_function(q1,q2,r):
    return q1*q2/(4*(r**2))

def energy_function(A,B,q1,q2,r):
    E = A/(r**12) - B/(r**6) + q1*q2/(4*(r**2))
    return E

def intermolecular_Energy(parm_stuff,frame,start1,stop1,start2,stop2):
    # start1, start2, stop1, stop2,
    Eint = 0
    Evdw = 0
    Ees = 0 
#   print start1, stop1, start2, stop2

#   print "i,j,A,B,q1,q2,r,Eint"
    for i in range(start1,stop1):
        for j in range(start2,stop2):

             q1 = parm_stuff.CHARGE[i-1]
             q2 = parm_stuff.CHARGE[j-1]
             A  = parm_stuff.M_LJA[ parm_stuff.ATOM_TYPE_INDEX[i-1]-1][parm_stuff.ATOM_TYPE_INDEX[j-1]-1] 
             #[i-1] because i is one value higher in initial range supplied; ATOM_TYPE_INDEX is also one value off to pass to matrix
             B  = parm_stuff.M_LJB[ parm_stuff.ATOM_TYPE_INDEX[i-1]-1][parm_stuff.ATOM_TYPE_INDEX[j-1]-1]

             r = distance(frame.cords[i-1],frame.cords[j-1])

             Eint = Eint+energy_function(A,B,q1,q2,r)
             Evdw = Evdw+vdw_energy_function(A,B,r)
             Ees  = Ees+es_energy_function(q1,q2,r)
#            print i,j,A,B,q1,q2,r,Eint

    return (Eint,Evdw,Ees)


def find_range(list):
  # examples: 1-4,7-10,34-59
  list_split = list.split(',')
  int_list = []

  for i in range(len(list_split)):
      interval = list_split[i].split('-')
      if (len(interval) == 1): 
         tmp_int_list = [int(interval[0])] #HOLDEN: 11-13-11; Note; for single values, must be list, not int
      elif (len(interval) == 2): 
         tmp_int_list = range(int(interval[0]),int(interval[1])+1)
      else:
        print "error"
        sys.exit(0)
      for i in range(len(tmp_int_list)):
         int_list.append(tmp_int_list[i])
  
  return int_list
     
def obtain_fps(frames,parm_stuff,int_list1,list2_resid1,list2_resid2):
  vdw_fp_frames = [] #Initialize matricies; going to append each frames' fp; NxM where N is residues and M is frames
  es_fp_frames = []
  for i in range(len(frames)):

    vdw_fp = []  #initialize array for fp for each frame
    es_fp = []
  
    for resid1 in int_list1:

       start1 = parm_stuff.RESIDUE_POINTER[resid1-1]
       stop1  = parm_stuff.RESIDUE_POINTER[resid1]

       start2 = parm_stuff.RESIDUE_POINTER[list2_resid1-1]
       if list2_resid2 == len(parm_stuff.RESIDUE_POINTER): #HOLDEN: 11-12-11 If lig is last residue then
         stop2  = len(parm_stuff.RESIDUE_ARRAY)+1 #Have the atoms go to last atom in list
       else:
         stop2  = parm_stuff.RESIDUE_POINTER[list2_resid2] 

       (Eint,Evdw,Ees) = intermolecular_Energy(parm_stuff,frames[i],start1,stop1,start2,stop2)
       vdw_fp.append(Evdw)
       es_fp.append(Ees)
    
    vdw_fp_frames.append(vdw_fp)
    es_fp_frames.append(es_fp)

  return (vdw_fp_frames,es_fp_frames)

def print_fp_frames(fp_frames,parm_stuff,outfile):
  f1 = open(outfile, 'w')
  header = "resid"
  for j in range(len(fp_frames)):
    header = header + ',' + str(j+1)
  f1.write(header + '\n')
  for i in range(len(fp_frames[0])): #Note, because each line is a list of N residues' fps, loop over these first; changes to vertical orientation

    temp_line = str(parm_stuff.RESIDUE_LABEL[i]).strip(' ') + str(i+1)
    for j in range(len(fp_frames)):
       temp_line = temp_line + "," + str(fp_frames[j][i])
    f1.write(temp_line + '\n')
  f1.close()

def meanstdv(a):
  n, mean, std = len(a), 0, 0 
  for i in range(len(a)): 
    mean = mean + float(a[i]) 
  mean = mean / float(n) 

  for i in range(len(a)): 
    std = std + (float(a[i]) - mean)**2 
  std = (std / float(n-1))**(0.5) 

  return (mean, std)


def pearson(a,b):
  (mean_a,SD_a) = meanstdv(a)
  (mean_b,SD_b) = meanstdv(b)

  summ = 0
  for i in range(len(a)):
    summ = summ + ((a[i] - mean_a)*(b[i] - mean_b))

  r = summ / ((len(a)-1) * SD_a * SD_b )

  return r


def euclidean_distance(a,b):
  if len(a) != len(b):
    print "Lengths of comparison arrays not equal.  Check reference."
    return

  d_squared = 0
  for i in range(len(a)):
    d_squared = d_squared + (a[i] - b[i])**(2.0)
  d = d_squared**(0.5)

  return d

def norm(a):
  temp = 0
  for i in range(len(a)):
    temp = temp + a[i]**(2.0)
  norm = temp**(0.5)
  return norm

def normalized_euclidean_distance(a,b):
  norm_a = norm(a)
  norm_b = norm(b)

  d = 0
  for i in range(len(a)):
    d = d + ((a[i]/norm_a) - (b[i]/norm_b))**(2.0)
  norm_d = d**(0.5)

  return norm_d


def comparison(ref,traj,method,type):
  #Accepts a reference vector, a trajectory vector of vectors and a comparison method

  if method == "d":
    filename = "trj.d." + type + ".txt"
    file = open(filename,'w')
    for i in range(len(traj)):
      d = euclidean_distance(ref[0],traj[i])
      file.write(str(d)+'\n')
    file.close()

  elif method == "r":
    filename = "trj.r." + type + ".txt"
    file = open(filename,'w')
    for i in range(len(traj)):
      r = pearson(ref[0],traj[i])
      file.write(str(r)+'\n')
    file.close()

  elif method == "n":
    filename = "trj.norm_d." + type + ".txt"
    file = open(filename,'w')
    for i in range(len(traj)):
      n = normalized_euclidean_distance(ref[0],traj[i])
      file.write(str(n)+'\n')
    file.close()
  
  elif method == "all":
    filename_d = "trj.d." + type + ".txt"
    fd = open(filename_d,'w')
    filename_r = "trj.r." + type + ".txt"
    fr = open(filename_r,'w')
    filename_n = "trj.norm_d." + type + ".txt"
    fn = open(filename_n,'w')
    for i in range(len(traj)):
      d = euclidean_distance(ref[0],traj[i])
      fd.write(str(d)+'\n')
      r = pearson(ref[0],traj[i])
      fr.write(str(r)+'\n')
      n = normalized_euclidean_distance(ref[0],traj[i])
      fn.write(str(n)+'\n')
    fd.close()
    fr.close()
    fn.close()





def main():

  if len(sys.argv) != 7: # if no input
        print "Input:";
        print "amber prmtop filename"
        print "amber reference filename"
        print "amber trajectory filename"
        print "residues list1 for species 1:  Loop over these residues, continuity not necessary; ex: 1-4,7-10,34-59"
        print "residues list2 for species 2:  Treat as one group, must be continuous; ex. 109; ex. 109-114"
        print "method of comparison: r for pearson, d for euclidean distance, n for normalized, or all for all three."
        return

  parmfile  = sys.argv[1]
  reffile   = sys.argv[2]
  crdfile   = sys.argv[3]
  list1     = sys.argv[4]
  list2     = sys.argv[5]
  method    = sys.argv[6]

  int_list1 = find_range(list1) #Generates array containing list of residues for comparison

  interval = list2.split('-') #assume list is continuous

  if ( len(interval) == 2):
     list2_resid1 = int(interval[0])
     list2_resid2 = int(interval[1])
  elif ( len(interval) == 1):
     list2_resid1 = int(interval[0])
     list2_resid2 = int(interval[0])
  else:
     print "Error: residues for species 2:  Treat as one group, must be continuous.  Ex. 109, or 109-115"
     sys.exit(0)

  parm_stuff =  parm_reader(parmfile) #Reads in amber parm file
  #RESIDUE_LABEL = parm_reader(parmfile) #Reads in amber parm file
  frames = cord_reader(crdfile,len(parm_stuff.RESIDUE_ARRAY)) #Reads frames of trajectory and generates matrix of values
  refframe = cord_reader(reffile,len(parm_stuff.RESIDUE_ARRAY)) #Reads frames of reference and generates matrix of values

  print "There are " + str(len(frames)) + " in the trajectory."
  print "There are " + str(len(refframe)) + " in the reference."

  (vdw_fp_frames,es_fp_frames) = obtain_fps(frames,parm_stuff,int_list1,list2_resid1,list2_resid2) #Generate fp arrays
  (vdw_fp_ref,es_fp_ref) = obtain_fps(refframe,parm_stuff,int_list1,list2_resid1,list2_resid2) #Generate fp arrays

### The following 4 lines are original in Patrick's script to calculate the footprints for a reference and several frames in a trajectory. Saved for future use. 
  #print_fp_frames(vdw_fp_frames,"trj.vdw.csv") #Generates csv containing vdw_fp for each residue and frame
  #print_fp_frames(es_fp_frames,"trj.es.csv") #Generates csv containing es_fp for each residue and frame
  #print_fp_frames(vdw_fp_ref,"ref.vdw.csv") #Generates csv containing vdw_fp for each residue in reference
  #print_fp_frames(es_fp_ref,"ref.es.csv") #Generates csv containing es_fp for each residue in reference

### Single-point footprint calculations
  print_fp_frames(vdw_fp_frames,parm_stuff,"fp.vdw.csv") #Generates csv containing vdw_fp for each residue
  print_fp_frames(es_fp_frames,parm_stuff,"fp.es.csv") #Generates csv containing es_fp for each residue
  #print_fp_frames(vdw_fp_ref,"ref.vdw.csv") #Generates csv containing vdw_fp for each residue in reference
  #print_fp_frames(es_fp_ref,"ref.es.csv") #Generates csv containing es_fp for each residue in reference

### Footprint comparison
  #comparison(vdw_fp_ref,vdw_fp_frames,method,"vdw")
  #comparison(es_fp_ref,es_fp_frames,method,"es")

main()

