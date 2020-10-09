import os
import numpy as np
import matplotlib.pyplot as plt

# load data

query_points = np.load("results/query_points.npy")
implaus = np.load("results/implausibility.npy")

# set up triangulation for plotting implausibility

import matplotlib.tri

tri = matplotlib.tri.Triangulation(-(query_points[:,0]-80.)/40., (query_points[:,1]-0.1)/0.3)

# make figure

plt.figure(figsize=(4,3))
plt.tripcolor(query_points[:,0], query_points[:,1], tri.triangles, implaus,
              vmin = 0., vmax = 6., cmap="viridis_r")
cb = plt.colorbar()
cb.set_label("Implausibility")
plt.xlabel('Normal Stress (MPa)')
plt.ylabel('Shear to Normal Stress Ratio')
plt.tight_layout()
plt.savefig(os.path.join(os.getcwd(), "figure4.pdf"))
