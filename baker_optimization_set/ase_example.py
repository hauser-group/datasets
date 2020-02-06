from ase.io import read
from ase.calculators.qchem import QChem
from ase.optimize import BFGSLineSearch
from ase.calculators.calculator import Calculator, all_properties


class EvalCountingCalculator(Calculator):
    """Simplification of the LoggingCalculator to count ab-initio calls
    """
    implemented_properties = all_properties
    default_parameters = {}

    def __init__(self, calculator):
        Calculator.__init__(self)
        self.calculator = calculator
        self.n_evals = 0

    def calculate(self, atoms, properties, system_changes):
        Calculator.calculate(self, atoms, properties, system_changes)
        
        results = [self.calculator.get_property(prop, atoms)
                   for prop in properties]

        # Only count evaluation if system (typically the position)
        # has changed
        if system_changes:
            self.n_evals += 1
        self.results = dict(zip(properties, results))

# Write header for the results file
with open('BFGS_LS_results.txt', 'w') as fout:
    fout.write('id  evaluations\n')
# Loop over all molecules in the bechmark set
for i in range(1, 31):
    atoms = read('%02d.xyz' % i)
    calc = QChem(label='calculations/mol_%02d' % i,
                     scratch='calculations/scratch',
                     nt=4,
                     jobtype='force',
                     method='HF',
                     basis='STO-3G',
                     scf_algorithm='DIIS_GDM',
                     max_scf_cycles='500',
                     scf_convergence='7',
                     charge=0,
                     multiplicity=1)
    atoms.set_calculator(EvalCountingCalculator(calc))
    # Do first evaluation
    atoms.get_forces()
    # and switch scf_guess to read
    calc.set(scf_guess='read')

    opt = BFGSLineSearch(atoms)
    opt.run(fmax=0.01)
    # Append to the results file
    with open('BFGS_LS_results.txt', 'a') as fout:
        fout.write('%2d    % 3d\n' % (i, atoms.calc.n_evals))
