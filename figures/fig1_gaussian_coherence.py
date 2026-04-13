"""
Figure 1: Coherence under marginalization for jointly Gaussian variables.
Corresponds to Section 7 (Example 1), Theorems 4.19 and 4.20.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Publication settings
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 11
rcParams['axes.linewidth'] = 0.8
rcParams['xtick.major.width'] = 0.8
rcParams['ytick.major.width'] = 0.8
rcParams['text.usetex'] = False

rho_values = [0.1, 0.3, 0.5, 0.7, 0.9]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), sharey=True)

for idx, rho in enumerate(rho_values):
    # Pairwise mutual information for uniform correlation
    mi = -0.5 * np.log(1 - rho**2)
    
    # Scale threshold values
    s_vals = np.linspace(0, 1.5 * mi, 200)
    
    # Pre-marginalization: 3 pairs, all with MI = mi
    I_total_pre = 3 * mi
    # At scale s, only pairs with B_ij >= s contribute
    I_s_pre = np.where(s_vals <= mi, 3 * mi, 0.0)
    C_s_pre = I_s_pre / I_total_pre
    
    # Post-marginalization: 1 pair, MI = mi
    I_total_post = mi
    I_s_post = np.where(s_vals <= mi, mi, 0.0)
    C_s_post = I_s_post / I_total_post
    
    axes[0].plot(s_vals, C_s_pre, color=colors[idx], linewidth=1.5,
                 label=r'$\rho = {}$'.format(rho))
    axes[1].plot(s_vals, C_s_post, color=colors[idx], linewidth=1.5,
                 label=r'$\rho = {}$'.format(rho))

for ax in axes:
    ax.set_xlabel(r'Scale threshold $s$')
    ax.set_ylim(-0.05, 1.15)
    ax.set_xlim(left=0)
    ax.legend(fontsize=9, frameon=False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

axes[0].set_ylabel(r'Coherence $\mathcal{C}^{(\mathcal{O})}_s$')
axes[0].set_title('Pre-marginalization (3 variables)', fontsize=11)
axes[1].set_title('Post-marginalization (2 variables)', fontsize=11)

plt.tight_layout()
plt.savefig('/home/ubuntu/creativity-model/figures/fig1_gaussian_coherence.pdf',
            dpi=300, bbox_inches='tight')
plt.savefig('/home/ubuntu/creativity-model/figures/fig1_gaussian_coherence.png',
            dpi=300, bbox_inches='tight')
print("Figure 1 saved.")
