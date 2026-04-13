"""
Figure 4: Visual comparison of frameworks.
Radar/spider chart showing the structural properties of each framework.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 10
rcParams['axes.linewidth'] = 0.8

categories = [
    'Observer-dependent\ncoherence',
    'Scale-relative\ndestruction',
    'No fixed\nboundary',
    'No inference\narchitecture',
    'Domain\ngenerality'
]
N = len(categories)

# Scores (0 to 1) for each framework
# This framework, IIT, FEP, Decoherence
this_fw  = [1.0, 1.0, 1.0, 1.0, 1.0]
iit      = [0.0, 0.0, 0.0, 1.0, 0.4]
fep      = [0.3, 0.0, 0.0, 0.0, 0.5]
decohere = [0.0, 0.3, 0.0, 1.0, 0.2]

# Compute angle for each axis
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]  # close the loop

def close_data(data):
    return data + data[:1]

fig, ax = plt.subplots(1, 1, figsize=(7, 6), subplot_kw=dict(polar=True))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
labels = ['This framework', 'IIT', 'FEP', 'Decoherence']
datasets = [this_fw, iit, fep, decohere]

for data, color, label in zip(datasets, colors, labels):
    values = close_data(data)
    ax.plot(angles, values, 'o-', linewidth=1.8, markersize=5, label=label, color=color)
    ax.fill(angles, values, alpha=0.08, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=9)
ax.set_ylim(0, 1.15)
ax.set_yticks([0.25, 0.5, 0.75, 1.0])
ax.set_yticklabels(['0.25', '0.50', '0.75', '1.00'], fontsize=8)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9, frameon=False)
ax.set_title('Structural comparison of frameworks', fontsize=12, pad=20)

plt.tight_layout()
plt.savefig('/home/ubuntu/creativity-model/figures/fig4_framework_comparison.pdf', dpi=300, bbox_inches='tight')
plt.savefig('/home/ubuntu/creativity-model/figures/fig4_framework_comparison.png', dpi=300, bbox_inches='tight')
print("Figure 4 saved.")
