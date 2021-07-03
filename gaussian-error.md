# Gaussianのエラーとその対処法
「Error termination via Lnk1e in」の続きを確認する。
- 参考：https://computational-chemistry.com/top/gaussian-error-message/
- 参考：http://bbs.keinsci.com/thread-4829-1-1.html

## L502: Convergence failure
```
Convergence failure -- run terminated.
Error termination via Lnk1e in l502.exe
```
**原因**：SCFが収束しなかった。  
**対処法**：`SCF=qc`、`SCF=xqc`、`SCF=yqc`を試す。  

## L508: Convergence failure
```
Density matrix breaks symmetry, PCut= 6.91D-03
Density matrix has no symmetry -- integrals replicated.
Iteration  80 EE= -1377.03506721338     Delta-E=       -0.001137227868 Grad=4.268D-02
Gradient too large for Newton-Raphson -- use scaled steepest descent instead.
Convergence failure.
Error termination via Lnk1e in C:\G09W\l508.exe at Mon Jun 26 19:36:04 2017.
```
**原因**：QC法でSCFが収束しなかった。  
**対処法**：`SCF=qc`、`SCF=xqc`、`SCF=yqc`を止める。  

## L9999: Optimization stopped.
```
Error termination via Lnk1e in l9999.exe
```
このエラーの場合、より上の行にエラーの原因が書かれる。
### ケース１
```
Optimization stopped.
-- Wrong number of Negative eigenvalues: Desired= 1 Actual= 4
-- Flag reset to prevent archiving.
```
**原因**：Gaussianは、遷移状態の最適化の際に虚の振動数の個数をチェックし、1でなくなったときに強制終了する。  
**対処法**：`opt=()`の中に`NoEigenTest`を追加して虚の振動数のチェックを無効にする。  
### ケース２
```
Optimization stopped.
-- Number of steps exceeded, NStep= 100
-- Flag reset to prevent archiving.
```
**原因**：構造最適化が決められたステップ数で終了しなかった。  
**対処法１**：`Opt=()`の中に`MaxCycles=1024`を追加する。もしくはその値を増やす。  
**対処法２**：GaussView等で構造最適化のエネルギー変化を確認し、最もエネルギーが小さい構造か大局的に見て最適と思われる構造から構造最適化を再スタートする。  
具体的なオプション例：  
- `Opt=(MaxCycles=1024)`
- `Opt=(MaxStep=5, MaxCycles=1024) IOp(1/8=2) Int(Grid=UltraFine)`
- `Opt=()`に`Cartesian`を追加してデカルト座標で構造最適化を行う。
- `Opt=(MaxStep=5, NoTrustUpdate, GDIIS)`
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
**原因**：IRCアルゴリズムのGS2において構造最適化が収束しなかった。  
**対処法**：`IRC=()`の中に`LQA`を追加してLQAアルゴリズムを検討する。   

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
**原因**：最適化の最中に3原子が直線に並んでしまうと構造最適化が強制終了してしまうことがある。  
**対処法１**：`Opt=()`に`Cartesian`を追加してデカルト座標で構造最適化を行う。  
**対処法２**：エラーで終了してしまった構造最適化の最終構造を初期構造にして再度構造最適化を行う。  

## L101: End of file in ZSymb
```
C -1.21995   2.13345   0.
End of file in ZSymb.
Error termination via Lnk1e in l101.exe
```
**原因**：インプットファイルの最後に空行がない。  
**対処法**：最後に空行を追加する。  

## L301: End of file reading basis center; EOF while reading ECP pointer card
```
End of file reading basis center.
Error termination via Lnk1e in /home/gauuser/g09/l301.exe at Wed Mar  1 20:50:57 2017.
```
```
======================================================================================================
                                       Pseudopotential Parameters
======================================================================================================
  Center     Atomic      Valence      Angular      Power
  Number     Number     Electrons     Momentum     of R      Exponent        Coefficient   SO-Coeffient
======================================================================================================
EOF while reading ECP pointer card.
Error termination via Lnk1e in /home/gauuser/g09/l301.exe at Wed Mar  1 20:43:41 2017.
```
**原因**：インプットファイルの書き方、書く順番が間違っているか書くべきものが書いてない。  
**対処法**：`gen`、`pseudo=read`、`genecp`を書いている場合、必要な情報があるべき場所に書かれているか確認して修正する。  
 
## L101: Wanted a XXX as input; Found an XXX as input
インプット
```
#p B3LYP/6-31G(d)

Title

H 0. 0. 0.

```
アウトプット
```
Wanted an integer as input.
Found a string as input.
H                0. 0. 0.                                                      
?
Error termination via Lnk1e in C:\G09W\l101.exe at Sun Mar 26 17:48:52 2017.
Job cpu time:       0 days  0 hours  0 minutes  0.0 seconds.
File lengths (MBytes):  RWF=      5 Int=      0 D2E=      0 Chk=      1 Scr=      1
```
**原因**：インプットの書き方が間違っている。上の例ではスピンと電荷を書いていないため、整数が書かれるべきところに文字が書かれている、というエラーが出ている。  
**対処法**：インプットを修正する。  
 
## L101: Input Error Input Error Input Error Input Error Input Error Input Error
```
-------------------
Title Card Required
-------------------
Symbolic Z-matrix:
Charge =  0 Multiplicity = 1


Input Error Input Error Input Error Input Error Input Error Input Error

There are no atoms in this input structure !

Please fix the molecule specification section of your input and try again.

Input Error Input Error Input Error Input Error Input Error Input Error

Error termination via Lnk1e in C:\G09W\l101.exe at Wed Jan 16 20:26:00 2019.
Job cpu time:       0 days  0 hours  0 minutes  0.0 seconds.
File lengths (MBytes):  RWF=      5 Int=      0 D2E=      0 Chk=      1 Scr=      1
```
**原因**：分子の構造が書かれていない、書き方が間違っている。もしくは`geom=check`、`geom=allcheck`を書き忘れているなど。  
**対処法**：キーワードのチェックや空行の数などを修正する。  
 
## L202: Problem with the distance matrix
```
Small interatomic distances encountered:      6     1     7     2     8     3     9     4    10     5
Problem with the distance matrix.
Error termination via Lnk1e in C:\G09W\l202.exe at Wed Jan 16 20:33:11 2019.
```
**原因**：入力した構造内に原子間距離が短い部分がある。特に、原子が重なっているなど。X線構造を入力にした時のディスオーダー構造に注意。  
**対処法**：GaussViewなどを用いて初期構造を修正する。余分な原子は削除するなど。  
 
## L202: Atoms too close
```
Small interatomic distances encountered:
     2    1 5.00D-02
Atoms too close.
Error termination via Lnk1e in C:\G09W\l202.exe at Wed Jan 16 20:38:12 2019.
```
**原因**：入力した構造内に原子間距離が短い部分がある。  
**対処法**：GaussViewなどを用いて初期構造を修正する。MM法を用いて粗く構造最適化を行うなど。  
 
## L1: Illegal IType or MSType generated by parse
```
----------
#p sp freq
----------
Illegal IType or MSType generated by parse.
Error termination via Lnk1e in C:\G09W\l1.exe at Thu Dec 07 13:58:19 2017.
Job cpu time:       0 days  0 hours  0 minutes  0.0 seconds.
File lengths (MBytes):  RWF=      1 Int=      0 D2E=      0 Chk=      1 Scr=      1
```
**原因**：共存できないキーワードがある。  
- `sp`と`freq`  
- `force`と`freq`  
など  

**対処法**：どちらも必要な場合は別のジョブで計算する。  

## L1: QPErr --- A syntax error was detected in the input line
```
------------------
#p M06-2X/6-31G(d)
------------------
QPErr --- A syntax error was detected in the input line.
#p M06-2X/6-31G(d)
       '
Last state= "GCL"
TCursr=      3656 LCursr=         7
Error termination via Lnk1e in C:\G09W\l1.exe at Wed Mar 06 14:19:36 2019.
Job cpu time:       0 days  0 hours  0 minutes  0.0 seconds.
```
**原因**：認識できないキーワードがある。上記のように`'`マークでその部分がハイライトされる。  
**対処法**：その部分を修正する。  
 
## L301: Atomic number out of range for XXX basis set
```
Rotational constants (GHZ):      0.0817250      0.0474806      0.0408748
Standard basis: 6-31G(d) (6D, 7F)
Atomic number out of range for 6-31G basis set.
Error termination via Lnk1e in /data2/G09/g09/l301.exe at Fri Mar 24 20:58:27 2017.
```
**原因**：指定した既定関数には含まれていない元素を指定した。  
**対処法**：別の既定関数を使用することを検討する。  
 
## L301: The combination of multiplicity X and XXX electrons is impossible
```
(Enter C:\G09W\l301.exe)
Standard basis: 6-31G(d) (6D, 7F)
Ernie: Thresh=  0.10000D-02 Tol=  0.10000D-05 Strict=F.
The combination of multiplicity 1 and     1 electrons is impossible.
Error termination via Lnk1e in C:\G09W\l301.exe at Sun Mar 26 18:00:32 2017.
Job cpu time:       0 days  0 hours  0 minutes  1.0 seconds.
File lengths (MBytes):  RWF=      5 Int=      0 D2E=      0 Chk=      1 Scr=      1
```
**原因**：電荷とスピン多重度の組み合わせが間違っている。  
**対処法**：  
 
## : 
```

```
**原因**：  
**対処法**：  
 
## : 
```

```
**原因**：  
**対処法**：  
 
## : 
```

```
**原因**：  
**対処法**：  
 
## : 
```

```
**原因**：  
**対処法**：  
 
## : 
```

```
**原因**：  
**対処法**：  
 
## : 
```

```
**原因**：  
**対処法**：  
 
## : 
```

```
**原因**：  
**対処法**：  
 
## : 
```

```
**原因**：  
**対処法**：  
 
## : 
```

```
**原因**：  
**対処法**：  
 
## : 
```

```
**原因**：  
**対処法**：  
 
## : 
```

```
**原因**：  
**対処法**：  

