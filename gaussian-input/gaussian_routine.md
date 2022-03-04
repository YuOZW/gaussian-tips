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
