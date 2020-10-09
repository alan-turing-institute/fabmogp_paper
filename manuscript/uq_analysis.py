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

valid_error = (validations.mean - validation_results)/np.sqrt(validations.unc)

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

# save results

np.save("results/input_points.npy", input_points)
np.save("results/validation_points.npy", validation_points)
np.save("results/hyperparameters.npy", gp.theta)
np.save("results/valid_error.npy", valid_error)
np.save("results/query_points.npy", query_points)
np.save("results/query_mean.npy", predictions.mean)
np.save("results/implausibility.npy", implaus)
np.save("results/NROY.npy", np.array(NROY, dtype=np.int64))
