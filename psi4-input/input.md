# 標準的なインプット
```
molecule mol {
0 1
H 0.0 0.0 0.0 
H 1.0 0.0 0.0

units angstrom
no_reorient
no_com
symmetry c1
}

set {
basis          def2-svp
scf_type       df
freeze_core    true
}

set_num_threads(18)
set_memory('80 GB')

energy('b3lyp')
```
