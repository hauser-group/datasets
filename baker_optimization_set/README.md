# Baker optimization bechmark

This dataset contains the xyz files of the 30 small molecules used by Baker [1]
to benchmark optimization algorithms. The PES is evaluated using the RHF
method and the STO-3G basis set. All molecules are uncharged and in a singlet
state.

## Results
Number of ab-initio evaluations (including the the first, therefore not the same as optimization cycles!)

| ID | Name                      | (1) |
|----|---------------------------|:---:|
| 01 | Water                     | 8   |
| 02 | Ammonia                   | 7   |
| 03 | Ethane                    | 7   |
| 04 | Acetylene                 | 7   |
| 05 | Allene                    | 7   |
| 06 | Hydroxysulfane            | 18  |
| 07 | Benzene                   | 5   |
| 08 | Methylamine               | 15  |
| 09 | Ethanol                   | 23  |
| 10 | Acetone                   | 15  |
| 11 | Disilyl-ether             | 17  |
| 12 | 1,3,5-Trisilacyclohexane  | 35  |
| 13 | Benzaldehyde              | 37  |
| 14 | 1,3-Difluorobenzene       | 17  |
| 15 | 1,3,5-Trifluorobenzene    | 12  |
| 16 | Neopentane                | 7   |
| 17 | Furan                     | 17  |
| 18 | Naphthalene               | 15  |
| 19 | 1,5-Difluoronaphthalene   | 25  |
| 20 | 2-Hydroxybicyclopentane   | 51  |
| 21 | ACHTAR10                  | 54  |
| 22 | ACANIL01                  | 53  |
| 23 | Benzidine                 | 34  |
| 24 | Pterin                    | 45  |
| 25 | Difuropyrazine            | 31  |
| 26 | Mesityl-oxide             | 42  |
| 27 | Histidine                 | -   |
| 28 | Dimethylpentane           | -   |
| 29 | Caffeine                  | -   |
| 30 | Menthone                  | -   |
|    | Sum                       |     |

(1) ASE (3.19.0b1) `BFGSLineSearch(maxstep=.2, c1=0.23, c2=0.46, alpha=10.0, stpmax=50.0)`

[1] Jon Baker, *Techniques for geometry optimization: A comparison of cartesian and natural internal coordinates*,  
    J. Comput. Chem, **14** (9), 1085-1100 (1993), [DOI: 10.1002/jcc.540140910](https://doi.org/10.1002/jcc.540140910)
