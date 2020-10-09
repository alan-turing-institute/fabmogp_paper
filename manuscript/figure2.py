import os
import numpy as np
import matplotlib.pyplot as plt

# load data needed for plotting

input_points = np.load("results/input_points.npy")
validation_points = np.load("results/validation_points.npy")
query_points = np.load("results/query_points.npy")
query_mean = np.load("results/query_mean.npy")
valid_error = np.load("results/valid_error.npy")

# set up triangulation for plotting simulator output

import matplotlib.tri

tri = matplotlib.tri.Triangulation(-(query_points[:,0]-80.)/40., (query_points[:,1]-0.1)/0.3)

# make plots

valid_include = (np.abs(valid_error) > 3.)

fig = plt.figure(figsize=(6.5,3))
fig.add_subplot(121)
plt.plot([x for x in range(len(valid_error))], valid_error,
         marker="o", color="C0", linewidth=0.)
plt.plot([-1., 11.], [-3., -3.], color="C1", linestyle="--", alpha=0.5)
plt.plot([-1., 11.], [3., 3.], color="C1", linestyle="--", alpha=0.5)
plt.xlabel("Validation point number")
plt.ylabel("Prediction standard error")

fig.add_subplot(122)
plt.tripcolor(query_points[:,0], query_points[:,1], tri.triangles,
              query_mean, vmin = 0., vmax = 250., cmap="viridis")
cb = plt.colorbar()
cb.set_label("Predicted seismic moment (m km)")
plt.plot(input_points[:,0], input_points[:,1],
         marker="o", color="white", linewidth=0.)
plt.plot(validation_points[~valid_include,0],
         validation_points[~valid_include,1],
         marker="o", color="black", linewidth=0.)
plt.plot(validation_points[valid_include, 0],
         validation_points[valid_include,1],
         marker="o", color="C3", linewidth=0.)
plt.xlabel('Normal Stress (MPa)')
plt.ylabel('Shear to Normal Stress Ratio')
plt.tight_layout()

fig.text(0.005, 0.95, "(a)")
fig.text(0.465, 0.95, "(b)")

plt.savefig(os.path.join(os.getcwd(), "figure2.pdf"))
