"""
Figure 2: Coherence under anesthetic suppression of long-lag coupling.
Corresponds to Section 8 (Example 2), Theorems 4.20 and 4.21.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 11
rcParams['axes.linewidth'] = 0.8
rcParams['xtick.major.width'] = 0.8
rcParams['ytick.major.width'] = 0.8

# Model parameters
n_channels = 5
n_pairs = n_channels * (n_channels - 1) // 2  # 10 pairs
tau_fast_max = 3     # fast lags: 1-3
tau_slow_min = 10    # slow lags: 10-20
tau_slow_max = 20

# Generate synthetic binding tensor values
# Fast coupling: strong, uniform across pairs
np.random.seed(42)
B_fast = np.ones((n_pairs, tau_fast_max)) * 0.15  # nats per pair per lag

# Slow coupling: moderate, decaying with lag
slow_lags = np.arange(tau_slow_min, tau_slow_max + 1)
B_slow_base = 0.08 * np.exp(-0.05 * (slow_lags - tau_slow_min))
B_slow = np.tile(B_slow_base, (n_pairs, 1))

# Total information
I_fast_total = B_fast.sum()
I_slow_total = B_slow.sum()
I_total = I_fast_total + I_slow_total

# Suppression levels
gamma_values = [1.0, 0.5, 0.3, 0.1, 0.01]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Scale parameter: temporal resolution threshold (inverse lag)
# Small s = fine scale (includes all lags), large s = coarse scale (only fast lags)
# We define s as the minimum lag included. s=1 includes all lags. s=10 includes only slow lags.
# Actually, let's define scale as maximum lag included (more intuitive)
s_values = np.arange(1, tau_slow_max + 1)

fig, ax = plt.subplots(1, 1, figsize=(7, 4.5))

eps_O = 0.15  # detection threshold

for idx, gamma in enumerate(gamma_values):
    coherence = []
    # After suppression: fast coupling unchanged, slow coupling multiplied by gamma
    I_total_gamma = I_fast_total + gamma * I_slow_total
    
    for s in s_values:
        # Information at scale s: sum of binding for lags <= s
        I_s = 0
        # Fast lags (1 to tau_fast_max)
        if s >= 1:
            fast_included = min(s, tau_fast_max)
            I_s += B_fast[:, :fast_included].sum()
        # Slow lags (tau_slow_min to min(s, tau_slow_max))
        if s >= tau_slow_min:
            slow_included = min(s, tau_slow_max) - tau_slow_min + 1
            I_s += gamma * B_slow[:, :slow_included].sum()
        
        C_s = I_s / I_total_gamma if I_total_gamma > 0 else 0
        coherence.append(C_s)
    
    label = r'$\gamma = {}$'.format(gamma)
    if gamma == 1.0:
        label = r'$\gamma = 1.0$ (awake)'
    elif gamma == 0.01:
        label = r'$\gamma = 0.01$ (deep anesthesia)'
    
    ax.plot(s_values, coherence, color=colors[idx], linewidth=1.8, label=label)

# Detection threshold
ax.axhline(y=eps_O, color='gray', linestyle='--', linewidth=1.0, alpha=0.7)
ax.text(tau_slow_max - 3, eps_O + 0.02, r'$\epsilon_{\mathcal{O}}$', fontsize=10, color='gray')

# Mark the fast/slow boundary
ax.axvline(x=tau_fast_max, color='gray', linestyle=':', linewidth=0.8, alpha=0.5)
ax.text(tau_fast_max + 0.3, 0.05, 'fast/slow\nboundary', fontsize=8, color='gray')

ax.set_xlabel(r'Maximum lag included (temporal scale)')
ax.set_ylabel(r'Coherence $\mathcal{C}^{(\mathcal{O})}_s$')
ax.set_title('Coherence under anesthetic suppression of long-lag coupling', fontsize=11)
ax.legend(fontsize=9, frameon=False, loc='center right')
ax.set_ylim(-0.05, 1.1)
ax.set_xlim(0.5, tau_slow_max + 0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('/home/ubuntu/creativity-model/figures/fig2_neural_suppression.pdf',
            dpi=300, bbox_inches='tight')
plt.savefig('/home/ubuntu/creativity-model/figures/fig2_neural_suppression.png',
            dpi=300, bbox_inches='tight')
print("Figure 2 saved.")
