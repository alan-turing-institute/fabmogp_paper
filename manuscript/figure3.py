import os
import numpy as np
import matplotlib.pyplot as plt

query_points = np.load("results/query_points.npy")
NROY = np.load("results/NROY.npy")

plt.figure(figsize=(4,3))
plt.plot(query_points[NROY, 0], query_points[NROY, 1], 'o')
plt.xlabel('Normal Stress (MPa)')
plt.ylabel('Shear to Normal Stress Ratio')
plt.xlim((-120., -80.))
plt.ylim((0.1, 0.4))
plt.tight_layout()
plt.savefig(os.path.join(os.getcwd(), "figure3.pdf"))
