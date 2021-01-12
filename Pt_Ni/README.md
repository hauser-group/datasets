Dataset for the development of machine learning based potentials.

Each .json file contains the geometries (listed in the fields 'symbols' and 'positions') and the results of a spin unrestricted DFT calculation using the PBE functional and a wavefunction cutoff of 40 Ryd and a density cutoff of 400 Ryd ('e_dft_tot' and 'forces_dft'). The field 'e_dft_bond' contains the bonding energy, that is the total energy minus the energy of isolated Pt and Ni atoms:  
E<sub>bond</sub> = E<sub>tot</sub> - N<sub>Pt</sub> E<sub>Pt</sub> - N<sub>Ni</sub> E<sub>Ni</sub>  
