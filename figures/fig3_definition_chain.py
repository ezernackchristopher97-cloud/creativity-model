"""
Figure 3: Definition dependency chain of the framework.
Shows the logical flow from underlying reality through observer interface
to coherence and representability.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.patches as mpatches

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 10
rcParams['axes.linewidth'] = 0.8

fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

# Define boxes and positions
boxes = [
    (0.5, 3.5, r'$\mathcal{R}$' + '\nUnderlying\nReality'),
    (2.0, 3.5, r'$\mathcal{O}$' + '\nObserver\nInterface'),
    (3.5, 3.5, r'$I_{\mathcal{O}}$' + '\nInterface\nMap'),
    (5.0, 3.5, r'$\Sigma_{\mathcal{O}}$' + '\nState\nSpace'),
    (6.5, 4.2, r'$(E, \nu)$' + '\nDecomposition'),
    (6.5, 2.8, r'$\{\mathcal{F}_s\}$' + '\nFiltration'),
    (8.0, 4.2, r'$\mathcal{B}_{ij}$' + '\nBinding\nTensor'),
    (8.0, 2.8, r'$\mathcal{I}_s[x]$' + '\nScale-Cond.\nInformation'),
    (9.5, 3.5, r'$\mathcal{C}^{(\mathcal{O})}_s$' + '\nCoherence'),
]

# Additional branch
boxes2 = [
    (5.0, 1.2, r'$\mathcal{D}_{\mathcal{O}}, \mathcal{T}_{\mathcal{O}}, \mathcal{V}_{\mathcal{O}}$' + '\nDistinctions, Transforms, Invariants'),
    (7.5, 1.2, r'$\mathfrak{M}_{\mathcal{O}}$' + '\nInduced Math'),
    (9.5, 1.2, r'$\Psi_{\mathcal{O}}$' + '\nRepresentability'),
]

box_w = 1.3
box_h = 0.9

def draw_box(ax, cx, cy, text, color='#E8F0FE'):
    rect = mpatches.FancyBboxPatch(
        (cx - box_w/2, cy - box_h/2), box_w, box_h,
        boxstyle="round,pad=0.05",
        facecolor=color, edgecolor='#333333', linewidth=1.0
    )
    ax.add_patch(rect)
    ax.text(cx, cy, text, ha='center', va='center', fontsize=8, 
            fontweight='normal', linespacing=1.3)

# Draw main chain boxes
for cx, cy, text in boxes:
    draw_box(ax, cx, cy, text)

# Draw lower branch boxes
for cx, cy, text in boxes2:
    draw_box(ax, cx, cy, text, color='#FFF3E0')

# Draw arrows (main chain)
arrow_props = dict(arrowstyle='->', color='#333333', lw=1.2)
# R -> O
ax.annotate('', xy=(2.0 - box_w/2, 3.5), xytext=(0.5 + box_w/2, 3.5), arrowprops=arrow_props)
# O -> I_O
ax.annotate('', xy=(3.5 - box_w/2, 3.5), xytext=(2.0 + box_w/2, 3.5), arrowprops=arrow_props)
# I_O -> Sigma
ax.annotate('', xy=(5.0 - box_w/2, 3.5), xytext=(3.5 + box_w/2, 3.5), arrowprops=arrow_props)
# Sigma -> (E,nu)
ax.annotate('', xy=(6.5 - box_w/2, 4.2), xytext=(5.0 + box_w/2, 3.7), arrowprops=arrow_props)
# Sigma -> Filtration
ax.annotate('', xy=(6.5 - box_w/2, 2.8), xytext=(5.0 + box_w/2, 3.3), arrowprops=arrow_props)
# (E,nu) -> B_ij
ax.annotate('', xy=(8.0 - box_w/2, 4.2), xytext=(6.5 + box_w/2, 4.2), arrowprops=arrow_props)
# Filtration -> I_s
ax.annotate('', xy=(8.0 - box_w/2, 2.8), xytext=(6.5 + box_w/2, 2.8), arrowprops=arrow_props)
# B_ij -> Coherence
ax.annotate('', xy=(9.5 - box_w/2, 3.7), xytext=(8.0 + box_w/2, 4.0), arrowprops=arrow_props)
# I_s -> Coherence
ax.annotate('', xy=(9.5 - box_w/2, 3.3), xytext=(8.0 + box_w/2, 3.0), arrowprops=arrow_props)

# Lower branch arrows
# Sigma -> D,T,V
ax.annotate('', xy=(5.0 - box_w/2, 1.2), xytext=(5.0, 3.5 - box_h/2), arrowprops=arrow_props)
# D,T,V -> M_O
ax.annotate('', xy=(7.5 - box_w/2, 1.2), xytext=(5.0 + box_w/2, 1.2), arrowprops=arrow_props)
# M_O -> Psi_O
ax.annotate('', xy=(9.5 - box_w/2, 1.2), xytext=(7.5 + box_w/2, 1.2), arrowprops=arrow_props)
# Coherence -> Psi_O
ax.annotate('', xy=(9.5, 1.2 + box_h/2), xytext=(9.5, 3.5 - box_h/2), arrowprops=arrow_props)

plt.tight_layout()
plt.savefig('/home/ubuntu/creativity-model/figures/fig3_definition_chain.pdf', dpi=300, bbox_inches='tight')
plt.savefig('/home/ubuntu/creativity-model/figures/fig3_definition_chain.png', dpi=300, bbox_inches='tight')
print("Figure 3 (definition chain) saved.")
