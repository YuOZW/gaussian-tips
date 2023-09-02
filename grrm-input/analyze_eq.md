## EQリストの整理（同一分子判定）
```python
#-------------------------------------------------------------------------------
# Name:       myGRRMl01
# Purpose:     summarize EQ list from GRRM program
#
# Author:     Ozawa
#
# Created:     21 /04 /2018
# Copyright:   (c) Ozawa 2018
# Licence:     Yu Ozawa
#-------------------------------------------------------------------------------
 
import os.path
import sys
from sys import argv
import numpy as np
from scipy import optimize
import math
 
#00 : Initialize ###############################################################
 
try:
              fin = open("/home/b/b35072/python/element","r")
              line = fin.readline()
              element = line.split(',')
except:
              print("Error 00: element file load error!")
              sys.exit()
 
mol_list = []
THRED_STD = 10
 
#01 : Input log file ###########################################################
 
flag_EQ = False
flag_PT = False
flag_TS = False
 
if len(argv) == 1:
              fname = input("Please input job name without _EQ_list.log\n")
elif len(argv) == 2:
              fname = argv[1]
else:
              print("Error 01: too many argument!")
              sys.exit()
 
fname_EQ = fname + "_EQ_list.log"
fname_PT = fname + "_PT_list.log"
fname_TS = fname + "_TS_list.log"
 
if os.path.isfile(fname_EQ):
              flag_EQ = True
if os.path.isfile(fname_PT):
              flag_PT = True
if os.path.isfile(fname_TS):
              flag_TS = True
              flag_PT = False
if not (flag_EQ or flag_PT or flag_TS):
              print("Error 01: EQ, PT or TS list log files are not exist!")
              sys.exit()
 
#01 : Analyze EQ list ##########################################################
 
def dist2(crd1):
              return crd1[0] ** 2 + crd1[1] ** 2 + crd1[2] ** 2
 
def analyze_EQ(fname):
              fin = open(fname,"r")
              fout = open(fname[:-3] + "xyz","w")
              mol_list = []
              e_list = []
              s_list = []
              n_list = []
              try:
                            line = fin.readline()
                            line = fin.readline()
                            while line:
                                          title = fin.readline()
                                          mol1 = []
                                          n_atoms = 0
                                          while line:
                                                        line = fin.readline()
                                                        if line.startswith("Energy"):
                                                                      break
                                                        n_atoms += 1
                                                        m1_n = element.index(line.split()[0].title())
                                                        m1_x = float(line.split()[1])
                                                        m1_y = float(line.split()[2])
                                                        m1_z = float(line.split()[3])
                                                        mol1.append([m1_n, m1_x, m1_y, m1_z])
                                          m1_e = float(line.split()[2])
                                          line = fin.readline()
                                          m1_s = float(line.split()[2])
                                         
                                          fout.write(str(n_atoms) + "\n")
                                          fout.write("EQ" + title.split()[4][:-1].rjust(5) + "\n")
                                          for m in mol1:
                                                        fout.write(element[m[0]].ljust(2))
                                                        fout.write(str(m[1]).rjust(18))
                                                        fout.write(str(m[2]).rjust(18))
                                                        fout.write(str(m[3]).rjust(18))
                                                        fout.write("\n")
                                         
                                          while line:
                                                        if line == "\n":
                                                                      break
                                                        line = fin.readline()
                                          if len(mol_list) == 0:
                                                        mol_list.append(mol1)
                                                        e_list.append(m1_e)
                                                        s_list.append(m1_s)
                                                        n_list.append([int(title.split()[4][:-1])])
                                          else:
                                                        same_str = False
                                                        dist_mat1 = []
                                                        for i in range(n_atoms):
                                                                      for j in range(0,i):
                                                                                    dist_x = mol1[i][1] - mol1[j][1]
                                                                                    dist_y = mol1[i][2] - mol1[j][2]
                                                                                    dist_z = mol1[i][3] - mol1[j][3]
                                                                                    dist = dist2([dist_x, dist_y, dist_z])
                                                                                    dist_mat1.append([mol1[i][0], mol1[j][0], dist])
                                                        dist_mat1.sort(key=lambda x:x[2])
                                                        dist_mat1.sort(key=lambda x:x[1])
                                                        dist_mat1.sort(key=lambda x:x[0])
                                                        for mol2 in mol_list:
                                                                      dist_mat2 = []
                                                                      for i in range(n_atoms):
                                                                                    for j in range(0,i):
                                                                                                  dist_x = mol2[i][1] - mol2[j][1]
                                                                                                  dist_y = mol2[i][2] - mol2[j][2]
                                                                                                  dist_z = mol2[i][3] - mol2[j][3]
                                                                                                  dist = dist2([dist_x, dist_y, dist_z])
                                                                                                  dist_mat2.append([mol2[i][0], mol2[j][0], dist])
                                                                      dist_mat2.sort(key=lambda x:x[2])
                                                                      dist_mat2.sort(key=lambda x:x[1])
                                                                      dist_mat2.sort(key=lambda x:x[0])
                                                                     
                                                                      dist_cmp = []
                                                                      weight = []
                                                                      for i in range(len(dist_mat1)):
                                                                                    dist_cmp.append((dist_mat1[i][2] - dist_mat2[i][2]))
                                                                                    weight.append( dist_mat1[i][0] + dist_mat2[i][1] )
                                                                      wt_std = (sum([(i*j-0.0)**2 for i,j in zip(dist_cmp,weight)]) /
                                                                                                  sum([i*j for i,j in zip(weight,weight)]))
                                                                      if wt_std < THRED_STD:
                                                                                    same_str = True
                                                                                    if m1_e < e_list[mol_list.index(mol2)]:
                                                                                                  e_list[mol_list.index(mol2)] = m1_e
                                                                                    if m1_s < s_list[mol_list.index(mol2)]:
                                                                                                  s_list[mol_list.index(mol2)] = m1_s
                                                                                    n_list[mol_list.index(mol2)].append(int(title.split()[4][:-1]))
                                                                                    break
                                                        if not same_str:
                                                                      mol_list.append(mol1)
                                                                      e_list.append(m1_e)
                                                                      s_list.append(m1_s)
                                                                      n_list.append([int(title.split()[4][:-1])])
                            for i in range(len(n_list)):
                                          print(n_list[i])
                                          print("Energy : " + str(e_list[i]))
                                          print("Spin : " + str(s_list[i]))
                                          print("")
              except:
                            pass
              finally:
                            fin.close()
                            fout.close()
 
 
if flag_EQ == True:
              analyze_EQ(fname_EQ)
if flag_PT == True:
              analyze_EQ(fname_PT)
if flag_TS == True:
              analyze_EQ(fname_TS)
```
