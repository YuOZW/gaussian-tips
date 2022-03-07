# TS
```
%nproc=xx
%mem=xxGB
%chk=jobname.chk
# Opt=(CalcFC,TS,MaxCycle=256,NoEigenTest,MaxStep=5) Freq=NoRaman NoSymm iop(1/8=2)
wB97XD Def2SVP SCRF=(SMD,Solvent=THF) SCF=(XQC,Tight) Int=(Grid=SuperFineGrid)

Title Card Required

0 1
C        2.435782000     -2.646433000     -2.112917000
... structure ...
H       -5.091586000     -3.012120000     -1.619195000

```

# IRC
#### Forward
```
%nproc=xx
%mem=xxGB
%oldchk=oldjobname.chk
%chk=jobname.chk
# IRC=(Forward,RCFC,MaxPoints=80,MaxCycle=1024,StepSize=20,LQA) NoSymm
wB97XD Def2SVP SCRF=(SMD,Solvent=THF) SCF=(XQC,Tight) Int=(Grid=SuperFineGrid)
Guess=Read Geom=Allcheck
```
#### Reverse
```
%nproc=xx
%mem=xxGB
%oldchk=oldjobname.chk
%chk=jobname.chk
# IRC=(Reverse,RCFC,MaxPoints=80,MaxCycle=1024,StepSize=20,LQA) NoSymm
wB97XD Def2SVP SCRF=(SMD,Solvent=THF) SCF=(XQC,Tight) Int=(Grid=SuperFineGrid)
Guess=Read Geom=Allcheck
```
