# Simulation Plan

**Paper:** Observer-Interface Emergence of Formal Systems and Scale-Relative Informational Persistence  
**Author:** Christopher Ezernack  
**Date:** April 2026

---

## Overview

This document outlines the simulation plan for producing figures that correspond to the paper's formal results. Each simulation is matched to a specific theorem or example. All simulations use either analytically controlled synthetic data or real publicly available datasets. No fabricated trend lines or decorative visuals.

---

## Simulation 1: Gaussian Coherence Under Marginalization

**Corresponds to:** Section 7 (Example 1), Theorem 4.19, Theorem 4.20

**Objective:** Show that marginalization reduces total integrated relational information but preserves coherence at fine scales.

**Method:**
1. Generate jointly Gaussian $\mathbf{X} = (X_1, X_2, X_3)$ with covariance matrix parameterized by $\rho$.
2. Compute pairwise mutual information $\mathcal{B}_{ij} = -\frac{1}{2}\ln(1 - \rho^2)$ for all pairs.
3. Compute $\mathcal{I}[\mathbf{X}] = 3 \times \mathcal{B}_{ij}$.
4. Apply marginalization $T$: remove $X_3$.
5. Compute $\mathcal{I}[T(\mathbf{X})] = 1 \times \mathcal{B}_{12}$.
6. Define scale threshold $s$ and compute $\mathcal{C}^{(\mathcal{O})}_s$ for both pre- and post-marginalization.
7. Sweep $\rho \in \{0.1, 0.2, \ldots, 0.9\}$.

**Output figure:** Coherence $\mathcal{C}^{(\mathcal{O})}_s$ vs. scale threshold $s$, with curves for pre-marginalization (3 variables) and post-marginalization (2 variables), at multiple values of $\rho$.

**Figure specifications:**
- Vector format (PDF or SVG)
- Clean axes, no grid clutter
- Labels use paper notation ($\mathcal{C}^{(\mathcal{O})}_s$, $s$, $\rho$)
- Legend with $\rho$ values
- Two panels: left = pre-marginalization, right = post-marginalization

---

## Simulation 2: Transfer Entropy Under Anesthetic Suppression

**Corresponds to:** Section 8 (Example 2), Theorem 4.20, Theorem 4.21

**Objective:** Show that suppression of long-lag coupling (modeling anesthesia) causes apparent destruction at coarse temporal scales while preserving coherence at fine temporal scales.

**Method:**
1. Generate synthetic multivariate time series $\mathbf{X}(t)$ with $n = 5$ channels.
2. Introduce coupling structure: short-lag coupling (lags 1-3) and long-lag coupling (lags 10-20).
3. Compute symmetrized transfer entropy $\mathcal{B}_{ij}^{(\tau)}$ for each pair and lag.
4. Compute $\mathcal{I}[\mathbf{X}]$ by summing over all pairs and lags.
5. Apply transformation $T_\gamma$: multiply long-lag coupling by $\gamma \in \{0.01, 0.1, 0.3, 0.5, 1.0\}$.
6. Compute $\mathcal{I}_s[T_\gamma(\mathbf{X})]$ at multiple temporal scale thresholds.
7. Compute coherence $\mathcal{C}^{(\mathcal{O})}_s$ for each $\gamma$.

**Output figure:** Coherence $\mathcal{C}^{(\mathcal{O})}_s$ vs. temporal scale $s$ (lag threshold), with curves for different suppression levels $\gamma$.

**Figure specifications:**
- Vector format
- Clean axes
- Labels use paper notation
- Color-coded curves for $\gamma$ values
- Horizontal dashed line at $\epsilon_{\mathcal{O}}$ (detection threshold)

---

## Simulation 3: Observer Overlap Convergence

**Corresponds to:** Section 5 (Theorem 5.9)

**Objective:** Demonstrate monotone convergence of observer overlap under scale refinement.

**Method:**
1. Define two observers on a shared Gaussian system with $n = 10$ variables.
2. Observer 1 starts with a coarse filtration (block-averaged groups of 5).
3. Observer 2 starts with a different coarse filtration (block-averaged groups of 2 and 8).
4. Iteratively refine both filtrations toward the full sigma-algebra.
5. At each refinement step, compute $\Omega(\mathcal{O}_1(t), \mathcal{O}_2(t))$.

**Output figure:** $\Omega$ vs. refinement step $t$, showing monotone non-decreasing convergence toward 1.

**Figure specifications:**
- Vector format
- Single panel
- Clean axes
- Labels: $\Omega(\mathcal{O}_1(t), \mathcal{O}_2(t))$ on y-axis, refinement step $t$ on x-axis

---

## Simulation 4 (Future): Real EEG Under Anesthesia

**Corresponds to:** Section 8, Section 12 (Future Work)

**Objective:** Apply the framework to real EEG data from OpenNeuro ds003171.

**Method:**
1. Download EEG data for awake and propofol-sedated conditions.
2. Compute transfer entropy between all channel pairs at multiple lags.
3. Construct binding tensor and compute $\mathcal{I}[\mathbf{X}]$ for both conditions.
4. Compute coherence profiles $\mathcal{C}^{(\mathcal{O})}_s$ for both conditions.
5. Compare: does the framework correctly predict that coherence drops at coarse scales under anesthesia while persisting at fine scales?

**Status:** Deferred to after manuscript review. Requires data download and preprocessing pipeline.

---

## Figure Production Standards

All figures must satisfy:
- Vector quality (PDF or SVG output from matplotlib)
- Publication clean: no unnecessary grid lines, no decorative elements
- Readable in print (grayscale-safe color choices or distinguishable line styles)
- Clear labels using the paper's notation
- Consistent font sizes across all figures
- No fake trend lines
- No decorative visuals pretending to be evidence
- Each figure reviewed individually before finalization
