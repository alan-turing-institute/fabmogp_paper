import os
from earthquake import create_problem, run_simulation

name = "rough_example"
results_dir = os.path.join(os.getcwd(), "results")
fdfault_path = "/home/root/fabmogp/fdfault/"

create_problem((-100., 0.25, 1.), name=name, output_dir=results_dir, vy_snapshot=True)
run_simulation(n_proc=4, mpi_exec="/usr/bin/mpiexec",
               output_dir=results_dir, fdfault_exec=fdfault_path)
