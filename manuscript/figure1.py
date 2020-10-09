import os
import matplotlib.pyplot as plt
import fdfault.analysis

name = "rough_example"
results_dir = os.path.join(os.getcwd(), "results")

vybody = fdfault.analysis.output(name, "vybody", datadir = os.path.join(results_dir, "data"))
vybody.load()

ufault = fdfault.analysis.output(name, "ufault", os.path.join(results_dir, "data"))
ufault.load()

fig = plt.figure(figsize=(6.5,3))
fig.add_subplot(121)
plt.pcolormesh(vybody.x, vybody.y, vybody.vy, vmin=-2., vmax=2.,
               shading="gouraud", cmap="RdBu")
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

plt.savefig(os.path.join(os.getcwd(), "figure1.pdf"))
