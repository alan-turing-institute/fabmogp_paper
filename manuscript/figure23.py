import os
import numpy as np
import matplotlib.pyplot as plt
from mogp_functions import load_results
from mogp_emulator import fit_GP_MAP

np.random.seed("734849")

results_dir = os.path.join(os.getcwd(), "results/demo_localhost_16")

input_points, results, ed = load_results(results_dir)

with open("lhc_values.tex", "w") as outfile:
    for (ip, res) in zip(input_points, results):
        outfile.write("{:2f} & {:3f} & {:.3f} & {:.2f} \\".format(ip[0], ip[1], ip[2], res))
        outfile.write("\n")

gp = fit_GP_MAP(input_points, results)

with open("correlation_lengths.tex", "w") as outfile:
    outfile.write("{:.3f}, {:.3f}, and {:.3f}".format(np.sqrt(np.exp(-gp.theta[:3]))))

with open("covariance_scale.tex", "w") as outfile:
    outfile.write("{:.3f}".format(np.sqrt(np.exp(gp.theta[3]))))

analysis_points = 10000
threshold = 3.

query_points = ed.sample(analysis_points)
predictions = gp.predict(query_points)

# set up history matching

hm = mogp_emulator.HistoryMatching(obs=known_value, expectations=predictions,
                                   threshold=threshold)

implaus = hm.get_implausibility()
NROY = hm.get_NROY()

# make some plots

plt.figure(figsize=(4,3))
plt.plot(query_points[NROY, 0], query_points[NROY, 1], 'o')
plt.xlabel('Normal Stress (MPa)')
plt.ylabel('Shear to Normal Stress Ratio')
plt.xlim((-120., -80.))
plt.ylim((0.1, 0.4))
plt.tight_layout()
plt.savefig("figure2.pdf")

import matplotlib.tri

plt.figure(figsize=(4,3))
tri = matplotlib.tri.Triangulation(-(query_points[:,0]-80.)/40., (query_points[:,1]-0.1)/0.3)
plt.tripcolor(query_points[:,0], query_points[:,1], tri.triangles, implaus,
              vmin = 0., vmax = 6., cmap="viridis_r")
cb = plt.colorbar()
cb.set_label("Implausibility")
plt.xlabel('Normal Stress (MPa)')
plt.ylabel('Shear to Normal Stress Ratio')
plt.tight_layout()
plt.savefig("figure3.pdf")