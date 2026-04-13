"""
Figure 3: Monotone convergence of observer overlap under scale refinement.
Corresponds to Section 5 (Theorem 5.9).

The theorem states that under pure scale refinement (same E, nu, B_ij),
overlap is non-decreasing. We model this by having both observers start
with coarse sigma-algebras and refine them. The key is that both observers
share the same underlying binding tensor and measure.

Implementation: Each observer has a partition of [n] variables. At each step,
both refine. The "representable set" for an observer is the set of variable
pairs (i,j) whose block-averaged MI exceeds a threshold. As partitions
become finer, more individual pairs become visible, and the two observers'
representable sets converge.
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

np.random.seed(42)

n = 16
# Strong within-cluster correlation, moderate cross-cluster
Sigma = 0.05 * np.ones((n, n))
np.fill_diagonal(Sigma, 1.0)
for c in range(4):
    for i in range(4*c, 4*c+4):
        for j in range(4*c, 4*c+4):
            if i != j:
                Sigma[i,j] = 0.6

def mi(rho):
    if abs(rho) < 1e-12: return 0.0
    if abs(rho) >= 0.999: return 5.0
    return -0.5 * np.log(1 - rho**2)

B = np.zeros((n,n))
for i in range(n):
    for j in range(i+1,n):
        B[i,j] = mi(Sigma[i,j])
        B[j,i] = B[i,j]

threshold = 0.01

def representable_set(partition):
    """
    For a given partition, the observer can detect:
    - All pairs within the same block (individual-level MI visible)
    - Pairs across blocks: only if the average MI between blocks > threshold
    
    Under pure scale refinement, within-block pairs are always detected.
    Cross-block pairs are detected based on block-averaged MI.
    """
    # Map each variable to its block index
    var_to_block = {}
    for bi, block in enumerate(partition):
        for v in block:
            var_to_block[v] = bi
    
    detected = set()
    for i in range(n):
        for j in range(i+1, n):
            if B[i,j] < threshold:
                continue
            bi = var_to_block[i]
            bj = var_to_block[j]
            if bi == bj:
                # Same block: always detected
                detected.add((i,j))
            else:
                # Cross-block: detected if block-avg MI > threshold
                block_i = list(partition[bi])
                block_j = list(partition[bj])
                avg_mi = np.mean([B[ii,jj] for ii in block_i for jj in block_j])
                if avg_mi > threshold:
                    detected.add((i,j))
    return detected

def refine(partition):
    """Split the largest block in half."""
    new_p = list(partition)
    sizes = [len(b) for b in new_p]
    idx = np.argmax(sizes)
    block = list(new_p[idx])
    if len(block) <= 1:
        return [tuple(b) for b in new_p]
    mid = len(block) // 2
    new_p[idx] = tuple(block[:mid])
    new_p.insert(idx+1, tuple(block[mid:]))
    return [tuple(b) for b in new_p]

# Observer 1: starts with [0..15] (single block, maximally coarse)
# Then refines: [0..7],[8..15] -> [0..3],[4..7],[8..11],[12..15] -> ...
p1_init = [tuple(range(n))]

# Observer 2: starts with interleaved partition
# [0,2,4,6,8,10,12,14], [1,3,5,7,9,11,13,15]
p2_init = [tuple(range(0,n,2)), tuple(range(1,n,2))]

T = 18
p1 = list(p1_init)
p2 = list(p2_init)

overlap_vals = []

for t in range(T):
    d1 = representable_set(p1)
    d2 = representable_set(p2)
    
    inter = d1 & d2
    union = d1 | d2
    
    omega = len(inter) / len(union) if len(union) > 0 else 0
    overlap_vals.append(omega)
    
    p1 = refine(p1)
    p2 = refine(p2)

fig, ax = plt.subplots(1, 1, figsize=(6.5, 4.5))
ax.plot(range(T), overlap_vals, 'o-', color='#1f77b4', linewidth=2.0, markersize=5)
ax.set_xlabel('Refinement step $t$')
ax.set_ylabel(r'Observer overlap $\Omega(\mathcal{O}_1(t), \mathcal{O}_2(t))$')
ax.set_title('Convergence of observer overlap under scale refinement', fontsize=11)
ax.set_ylim(-0.05, 1.1)
ax.set_xlim(-0.5, T - 0.5)
ax.axhline(y=1.0, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('/home/ubuntu/creativity-model/figures/fig3_observer_overlap.pdf', dpi=300, bbox_inches='tight')
plt.savefig('/home/ubuntu/creativity-model/figures/fig3_observer_overlap.png', dpi=300, bbox_inches='tight')
print("Figure 3 saved.")
print("Overlap values:", [f"{v:.4f}" for v in overlap_vals])
print(f"Partitions at end: p1 has {len(p1)} blocks, p2 has {len(p2)} blocks")
