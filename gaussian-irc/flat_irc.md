## 極めて遷移状態がフラットな場合のIRC
```
# irc=(CalcAll,Cartesian,maxpoints=500,maxcycle=64,stepsize=5) iop(1/7=1)
rwb97xd/Def2SVP scrf=(smd,solvent=thf) Integral(Grid=UltraFine)
```
![01-24_irc2_tot_ener](https://user-images.githubusercontent.com/45220906/142821058-973f6502-db11-4977-a1c8-a006fb7c997c.jpg)
- 活性化エネルギーが数kcal/molしかない遷移状態

## 別のバージョン
```
# irc=(CalcFC,recalc=5,Cartesian,maxpoints=80,maxcycle=1024,stepsize=20,LQA)
rwb97xd/Def2SVP scrf=(smd,solvent=thf) Integral(Grid=UltraFine)
iop(1/7=10) iop(1/8=1) iop(1/19=7)
```
- irc=(maxcycle=1024)：多めにとる。
- irc=(LQA)：local quadratic approximationの利用。GRRMと同じアルゴリズム。早い気がする。この計算はデフォルトのHPCではダメだった。
- irc=(stepsize=20)：ircの刻み幅を調整。デフォルトは10。
- Integral(Grid=UltraFine)：stepsizeを小さくするときにつける。
- iop(1/7=10)：収束判定。
- iop(1/8=1)：最適化の構造変化の大きさ。デフォルトは30。
- iop(1/19=7)：RFO without linear.
