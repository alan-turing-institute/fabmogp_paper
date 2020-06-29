from earthquake import create_problem, run_simulation
import numpy as np
import matplotlib.pyplot as plt
import fdfault.analysis

name = "rough_example"
fdfault_path = "/Users/edaub/Projects/fdfault/"

create_problem((-100., 0.25, 1.), name=name, output_dir=fdfault_path, vy_snapshot=True)
run_simulation(n_proc=4, mpi_exec="/usr/local/bin/mpiexec",
               output_dir=fdfault_path, fdfault_exec=fdfault_path)

vybody = fdfault.analysis.output(name, "vybody", datadir = fdfault_path+"data")
vybody.load()

ufault = fdfault.analysis.output(name, "ufault", datadir = fdfault_path+"data")
ufault.load()

fig = plt.figure(figsize=(6.5,3))
fig.add_subplot(121)
plt.pcolormesh(vybody.x, vybody.y, vybody.vy, vmin=-2., vmax=2., cmap="RdBu")
plt.plot(ufault.x, ufault.y, "k")
plt.axis("image")
plt.xlabel("Position along strike (km)")
plt.ylabel("Position across fault (km)")
cb = plt.colorbar()
cb.set_label("Fault normal particle velocity (m/s)")

fig.add_subplot(122)
plt.plot(ufault.x, ufault.U)
plt.xlabel("Position along strike (km)")
plt.ylabel("Final slip (m)")

plt.tight_layout()

fig.text(0.005, 0.95, "(a)")
fig.text(0.505, 0.95, "(b)")

plt.savefig("figure1.pdf")