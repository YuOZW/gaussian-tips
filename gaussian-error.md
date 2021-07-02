# Gaussianのエラーとその対処法
「Error termination via Lnk1e in」の続きを確認する。
- 参考：https://computational-chemistry.com/top/gaussian-error-message/
- 参考：http://bbs.keinsci.com/thread-4829-1-1.html

## L502: Convergence failure
```
Convergence failure -- run terminated.
Error termination via Lnk1e in l502.exe
```
原因：SCFが収束しなかった。  
対処法：SCF=qc、SCF=xqc、SCF=yqcを試す。  

## L508: Convergence failure
```
Density matrix breaks symmetry, PCut= 6.91D-03
Density matrix has no symmetry -- integrals replicated.
Iteration  80 EE= -1377.03506721338     Delta-E=       -0.001137227868 Grad=4.268D-02
Gradient too large for Newton-Raphson -- use scaled steepest descent instead.
Convergence failure.
Error termination via Lnk1e in C:\G09W\l508.exe at Mon Jun 26 19:36:04 2017.
```
原因：QC法でSCFが収束しなかった。  
対処法：SCF=qc、SCF=xqc、SCF=yqcを止める。  

## L9999: Optimization stopped.
```
Error termination via Lnk1e in l9999.exe
```
このエラーの場合、より上の行にエラーの原因が書かれる。
#### ケース１
```
Optimization stopped.
-- Wrong number of Negative eigenvalues: Desired= 1 Actual= 4
-- Flag reset to prevent archiving.
```
原因：Gaussianは、遷移状態の最適化の際に虚の振動数の個数をチェックし、1でなくなったときに強制終了する。  
対処法：opt=()の中に「NoEigenTest」を追加して虚の振動数のチェックを無効にする。  
#### ケース２
```
Optimization stopped.
-- Number of steps exceeded, NStep= 100
-- Flag reset to prevent archiving.
```
原因：構造最適化が決められたステップ数で終了しなかった。  
対処法１：Opt=()の中に「MaxCycles=1024」を追加する。もしくはその値を増やす。  
対処法２：GaussView等で構造最適化のエネルギー変化を確認し、最もエネルギーが小さい構造か大局的に見て最適と思われる構造から構造最適化を再スタートする。  
具体的なオプション例：  
- Opt=(MaxCycles=1024)
- Opt=(MaxStep=5, MaxCycles=1024) IOp(1/8=2) Int(Grid=UltraFine)
- Opt=()に「Cartesian」を追加してデカルト座標で構造最適化を行う。
- Opt=(MaxStep=5, NoTrustUpdate, GDIIS)
- 
## L123: Max corrector steps exceded; GS2 Optimization Failure
```
Delta-x Convergence NOT Met
    Maximum number of corrector steps exceded.
    Error termination via Lnk1e in l123.exe at Sun Sep  6 07:30:18 2015.
```
原因：デフォルトのIRCアルゴリズムであるHPCの補正ステップが収束しなかった。  
```
GS2 Optimization Failure.
    Error termination via Lnk1e in l123.exe
```
原因：IRCアルゴリズムのGS2において構造最適化が収束しなかった。  
対処法：IRC=()の中に「LQA」を追加してLQAアルゴリズムを検討する。   

## L103: Error in internal coordinate system; Linear angle in Bend; Linear angle in Tors; FormBX had a problem.
```
Bend failed for angle     1 -    11 -     3
    Tors failed for dihedral     9 -     1 -    11 -     3
    Tors failed for dihedral    10 -     1 -    11 -     3
    Tors failed for dihedral    12 -     1 -    11 -     3
    Tors failed for dihedral    14 -     3 -    11 -     1
    Tors failed for dihedral    17 -     3 -    11 -     1
    FormBX had a problem.
    Error termination via Lnk1e in l103.exe
```
```
GradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGrad
Berny optimization.
Using GEDIIS/GDIIS optimizer.
Linear angle in Bend.
Error termination via Lnk1e in /home/gauuser/g09/l103.exe at Sun Feb  5 05:25:49 2017.
```
```
NTrRot=    -1 NTRed=   798 NAtoms=    66 NSkip=   606 IsLin=F
Error in internal coordinate system.
Error termination via Lnk1e in l103.exe
```
```
Berny optimization.
Using GEDIIS/GDIIS optimizer.
Linear angle in Tors.
Error termination via Lnk1e in /home/program/g09/l103.exe at Thu Jun 25 22:29:51 2015.
```
原因：最適化の最中に3原子が直線に並んでしまうと構造最適化が強制終了してしまうことがある。  
対処法１：Opt=()に「Cartesian」を追加してデカルト座標で構造最適化を行う。  
対処法２：エラーで終了してしまった構造最適化の最終構造を初期構造にして再度構造最適化を行う。  
