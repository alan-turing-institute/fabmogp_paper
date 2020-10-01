import os
import numpy as np
import matplotlib.pyplot as plt
from mogp_functions import load_results
from mogp_emulator import fit_GP_MAP, HistoryMatching

def write_lhc_points(filename, input_points, results):
    with open("{}.tex".format(filename), "w") as outfile:
        for (ip, res) in zip(input_points, results):
            outfile.write("{:.2f} MPa & {:.3f} & {:.3f} & {:.2f} m km \\\\".format(ip[0], ip[1], ip[2], res))
            outfile.write("\n")


np.random.seed(73449)

results_dir = os.path.join(os.getcwd(), "results/training")

input_points, results, ed = load_results(results_dir)

write_lhc_points("lhc_values", input_points, results)

validation_dir = os.path.join(os.getcwd(), "results/validation")

validation_points, validation_results, ed = load_results(validation_dir)

write_lhc_points("validation_points", validation_points, validation_results)

gp = fit_GP_MAP(input_points, results)

with open("correlation_lengths.tex", "w") as outfile:
    outfile.write("{:.3f}, {:.3f}, and {:.3f}".format(*np.sqrt(np.exp(-gp.theta[:3]))))

with open("covariance_scale.tex", "w") as outfile:
    outfile.write("{:.3f}".format(np.sqrt(np.exp(gp.theta[3]))))

validations = gp.predict(validation_points)
    
analysis_points = 10000
threshold = 3.
known_value = 58.

query_points = ed.sample(analysis_points)
predictions = gp.predict(query_points)

# set up history matching

hm = HistoryMatching(obs=known_value, expectations=predictions,
                     threshold=threshold)

implaus = hm.get_implausibility()
NROY = hm.get_NROY()

# make some plots

plt.figure(figsize=(4,3))
plt.plot([x for x in len(validations.mean)],
         (validations.mean - validation_results)/np.sqrt(validations.unc),
         marker="o", color="blue", linewidth=0.)
plt.plot([-1., 11.], [-2., -2.], color="orange", linestyle="--", alpha=0.5)
plt.plot([-1., 11.], [2., 2.], color="orange", linestyle="--", alpha=0.5)
plt.yticks([-2., 0., 2.])
plt.xlabel("Validation point number")
plt.ylabel("Prediction standard deviations from the mean")
plt.tight_layout()
plt.savefig("figure2.pdf")

plt.figure(figsize=(4,3))
plt.plot(query_points[NROY, 0], query_points[NROY, 1], 'o')
plt.xlabel('Normal Stress (MPa)')
plt.ylabel('Shear to Normal Stress Ratio')
plt.xlim((-120., -80.))
plt.ylim((0.1, 0.4))
plt.tight_layout()
plt.savefig("figure3.pdf")

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
plt.savefig("figure4.pdf")
