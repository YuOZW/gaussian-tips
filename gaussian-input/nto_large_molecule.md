## 巨大なOpen-shellの分子のNTOを可視化したい時
インプットファイルで`#p`と`Pop=Regular`と`GFInput`を使う。

```
%nprocshared=2
%mem=4GB
%oldchk=filename_TD.chk
%chk=filename_NTO1.chk
#p wb97xd/def2svp scrf=(smd,solvent=thf) nosymm
Geom=AllCheck Guess=(Read,Only) Density=(Check,Transition=1) Pop=(Regular,NTO,SaveNTO) GFInput

```
---
アウトプットファイルをテキストで開き、
```
Alpha Natural Transition Orbital Coefficients:
Beta Natural Transition Orbital Coefficients:
```
これら二行を下のようにそれぞれ書き換える。
```
Alpha Molecular Orbital Coefficients:
Beta Molecular Orbital Coefficients:
```
このアウトプットファイルをChemCraftで開く。
