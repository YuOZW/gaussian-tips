`--link1--`と`geom=(allcheck,newdefinition,modredundant)`を使う。

```
%nprocshared=18
%mem=80GB
%chk=L2CuB_rad1_scan.chk
# opt=(modredundant,maxstep=10,maxcycle=1024,loose) wb97xd/genecp scrf=(smd,solvent=thf)
nosymm iop(1/8=5) scf=xqc

CuBSi2C38P2N2H68O5

0 1
 Cu                 0.84015863    0.60369123    0.92098541
 P                  0.02815478    2.74037897    1.25827671
 C                  1.28397917   -1.36534269    4.71241241
 C                  1.68467350   -2.50344231    3.77047079
 B                  1.19609133   -0.61627919    2.52056466
 O                  0.82089669   -0.33145542    3.84379866
 O                  1.79639265   -1.88440150    2.49054382
 H                  0.48813978   -1.64869431    5.40859393
 H                  2.13666511   -0.99515825    5.29647924
 H                  2.63858747   -2.96595405    4.04346966
 H                  0.92020814   -3.29074417    3.72717041
 C                  1.31994527    3.78091560    2.05495335
 H                  1.64160396    3.30553023    2.98757410
 H                  2.19078982    3.85465425    1.39448331
 H                  0.95161416    4.78990934    2.27416271
 C                 -1.36271022    2.90521382    2.44927690
 H                 -2.26678126    2.46202540    2.02039737
 H                 -1.11819278    2.36566348    3.37019305
 H                 -1.56193963    3.95619768    2.69019265
 C                 -0.53391555    3.84367274   -0.10482314
 H                 -1.37370399    3.37916089   -0.63185307
 H                 -0.85170018    4.82307607    0.27255104
 H                  0.28168512    3.98908017   -0.82072009
 P                  1.38553416    0.23930930   -1.28555738
 C                  3.18606163   -0.03914672   -1.53477434
 H                  3.42676194   -0.22593296   -2.58785072
 H                  3.74387700    0.83855562   -1.19083832
 H                  3.50349240   -0.89860536   -0.93504432
 C                  1.03447882    1.51764206   -2.56322077
 H                  1.56350755    2.44235083   -2.30893329
 H                  1.35176051    1.19300744   -3.56144292
 H                 -0.03923256    1.73180917   -2.58407525
 C                  0.66340733   -1.25876383   -2.06816025
 H                 -0.42423534   -1.15140783   -2.12682311
 H                  1.06154216   -1.41099873   -3.07831463
 H                  0.89052047   -2.13794604   -1.45666662
 C                 -2.79630397   -1.96820173    2.94351200
 H                 -3.57763648   -1.20393234    2.90737767
 H                 -1.94547522   -1.60439542    3.52723035
 H                 -3.20053938   -2.84853739    3.45929631
 C                 -2.36328822   -2.40026987    1.56101285
 H                 -3.21257902   -2.71735806    0.95459169
 C                 -1.25587746   -3.42854764    1.55405890
 H                 -0.38562977   -3.07092893    2.11217465
 H                 -1.62696649   -4.32849317    2.05996953
 H                 -0.95962207   -3.70268337    0.53773210
 Br                -1.72759021   -0.76025364    0.53246929

B 1 47 K
B 47 41 K
B 1 47 2.9221003
B 47 41 2.037564
B 1 47 F
B 47 41 F

P C B O H 0
6-31G(d)
****
Cu Br 0
SDD
****

Cu Br 0
SDD

--link1--
%nprocshared=18
%mem=80GB
%chk=L2CuB_rad1_scan.chk
# opt=(maxstep=10,maxcycle=1024,loose) wb97xd/chkbasis scrf=(smd,solvent=thf)
 nosymm iop(1/8=5) scf=xqc guess=read geom=(allcheck,newdefinition,modredundant)

B 1 47 K
B 47 41 K
B 1 47 2.82361
B 47 41 2.0415258
B 1 47 F
B 47 41 F

--link1--
%nprocshared=18
%mem=80GB
%chk=L2CuB_rad1_scan.chk
# opt=(maxstep=10,maxcycle=1024,loose) wb97xd/chkbasis scrf=(smd,solvent=thf)
 nosymm iop(1/8=5) scf=xqc guess=read geom=(allcheck,newdefinition,modredundant)

B 1 47 K
B 47 41 K
B 1 47 2.7378213
B 47 41 2.0537026
B 1 47 F
B 47 41 F

--link1--
%nprocshared=18
%mem=80GB
%chk=L2CuB_rad1_scan.chk
# opt=(maxstep=10,maxcycle=1024,loose) wb97xd/chkbasis scrf=(smd,solvent=thf)
 nosymm iop(1/8=5) scf=xqc guess=read geom=(allcheck,newdefinition,modredundant)

B 1 47 K
B 47 41 K
B 1 47 2.6230142
B 47 41 2.0525434
B 1 47 F
B 47 41 F

--link1--
%nprocshared=18
%mem=80GB
%chk=L2CuB_rad1_scan.chk
# opt=(maxstep=10,maxcycle=1024,loose) wb97xd/chkbasis scrf=(smd,solvent=thf)
 nosymm iop(1/8=5) scf=xqc guess=read geom=(allcheck,newdefinition,modredundant)

B 1 47 K
B 47 41 K
B 1 47 2.532553
B 47 41 2.1587014
B 1 47 F
B 47 41 F

--link1--
%nprocshared=18
%mem=80GB
%chk=L2CuB_rad1_scan.chk
# opt=(maxstep=10,maxcycle=1024,loose) wb97xd/chkbasis scrf=(smd,solvent=thf)
 nosymm iop(1/8=5) scf=xqc guess=read geom=(allcheck,newdefinition,modredundant)

B 1 47 K
B 47 41 K
B 1 47 2.4135475
B 47 41 2.5285666
B 1 47 F
B 47 41 F

--link1--
%nprocshared=18
%mem=80GB
%chk=L2CuB_rad1_scan.chk
# opt=(maxstep=10,maxcycle=1024,loose) wb97xd/chkbasis scrf=(smd,solvent=thf)
 nosymm iop(1/8=5) scf=xqc guess=read geom=(allcheck,newdefinition,modredundant)

B 1 47 K
B 47 41 K
B 1 47 2.3461592
B 47 41 2.8203316
B 1 47 F
B 47 41 F

--link1--
%nprocshared=18
%mem=80GB
%chk=L2CuB_rad1_scan.chk
# opt=(maxstep=10,maxcycle=1024,loose) wb97xd/chkbasis scrf=(smd,solvent=thf)
 nosymm iop(1/8=5) scf=xqc guess=read geom=(allcheck,newdefinition,modredundant)

B 1 47 K
B 47 41 K
B 1 47 2.334404
B 47 41 3.055713
B 1 47 F
B 47 41 F

--link1--
%nprocshared=18
%mem=80GB
%chk=L2CuB_rad1_scan.chk
# opt=(maxstep=10,maxcycle=1024,loose) wb97xd/chkbasis scrf=(smd,solvent=thf)
 nosymm iop(1/8=5) scf=xqc guess=read geom=(allcheck,newdefinition,modredundant)

B 1 47 K
B 47 41 K
B 1 47 2.3383455
B 47 41 3.2360144
B 1 47 F
B 47 41 F

--link1--
%nprocshared=18
%mem=80GB
%chk=L2CuB_rad1_scan.chk
# opt=(maxstep=10,maxcycle=1024,loose) wb97xd/chkbasis scrf=(smd,solvent=thf)
 nosymm iop(1/8=5) scf=xqc guess=read geom=(allcheck,newdefinition,modredundant)

B 1 47 K
B 47 41 K
B 1 47 2.34097
B 47 41 3.350228
B 1 47 F
B 47 41 F

```
