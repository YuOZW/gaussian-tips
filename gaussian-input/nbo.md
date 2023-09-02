## NBOの"molecular unit"を制御する
```
%nprocshared=xx
%mem=xxGB
%oldchk=oldfile.chk
%chk=newfile.chk
# rwb97xd/def2svp scrf=(smd,solvent=thf) pop=(NBOread,savenbos,savenpa) geom=checkpoint guess=read

Title Card Required

0 1

$NBO $END
$CHOOSE OK
LONE END
BOND S 1 2
D 1 2
T 1 2
END
$END
```
