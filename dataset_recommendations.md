# Dataset Recommendations Matched to Paper Sections

**Paper:** Observer-Interface Emergence of Formal Systems and Scale-Relative Informational Persistence  
**Author:** Christopher Ezernack  
**Date:** April 2026

---

## Overview

This document identifies real, publicly available datasets that can be used to empirically test the framework's predictions. Each recommendation is matched to a specific section of the paper and includes the dataset name, source, what it contains, and how it maps to the framework's constructs.

---

## 1. Neuroscience Example (Section 8): Anesthetic Suppression

### Dataset: OpenNeuro ds003171 (Anesthesia and Consciousness)

**Source:** [OpenNeuro](https://openneuro.org/datasets/ds003171)

**Contents:** EEG recordings from human subjects during wakefulness, propofol-induced sedation, and recovery. Multiple channels, high temporal resolution.

**Mapping to framework:**
- **Observer interface ($I_{\mathcal{O}}$):** EEG electrodes define the sensory structure. Each channel is a component $x_i$.
- **Binding tensor ($\mathcal{B}_{ij}$):** Compute symmetrized transfer entropy between channel pairs across temporal lags.
- **Scale filtration ($\{\mathcal{F}_s\}$):** Temporal lag threshold defines the scale. Short lags capture fast local coupling; long lags capture slow long-range coupling.
- **Transformation ($T_\gamma$):** Compare awake vs. anesthetized conditions. The anesthetic acts as the transformation.
- **Prediction:** The framework predicts that coherence at coarse temporal scales (long-lag transfer entropy) drops below threshold under anesthesia, while coherence at fine temporal scales (short-lag transfer entropy) is preserved. This is testable by computing $\mathcal{C}^{(\mathcal{O})}_s$ at multiple lag thresholds for both conditions.

### Alternative Dataset: OpenNeuro ds004148 (Propofol Anesthesia EEG)

**Source:** [OpenNeuro](https://openneuro.org/datasets/ds004148)

**Contents:** High-density EEG during propofol-induced loss of consciousness. Includes behavioral markers.

**Same mapping as above.** This dataset provides higher channel density, allowing for richer spatial structure in the binding tensor.

---

## 2. Statistical Mechanics Example (Section 7): Gaussian System

### Dataset: Synthetic (Analytically Controlled)

**Source:** Generated in simulation.

**Contents:** Jointly Gaussian random variables with specified covariance structure. Marginalization as transformation.

**Mapping to framework:**
- This example is analytically tractable and does not require empirical data.
- Simulations should use $n = 3$ variables with uniform correlation $\rho \in \{0.1, 0.3, 0.5, 0.7, 0.9\}$.
- Compute $\mathcal{I}[\mathbf{X}]$ and $\mathcal{I}[T(\mathbf{X})]$ in closed form.
- Plot coherence as a function of scale threshold for pre- and post-marginalization states.

---

## 3. Extended Neuroscience Application: Resting-State fMRI

### Dataset: Human Connectome Project (HCP) Resting-State fMRI

**Source:** [ConnectomeDB](https://db.humanconnectome.org/)

**Contents:** Resting-state fMRI from 1200 healthy adults. Parcellated time series available.

**Mapping to framework:**
- **Observer interface:** fMRI BOLD signal defines a coarse temporal observer (TR = 0.72s).
- **Binding tensor:** Compute pairwise mutual information or partial correlation between parcellated regions.
- **Scale filtration:** Frequency-band filtering defines the scale. Low-frequency fluctuations (0.01-0.1 Hz) vs. higher frequencies.
- **Use case:** Demonstrate that the same brain, observed at different temporal resolutions, yields different coherence profiles. This directly tests Theorem 4.21 (interface-dependent ontology).

---

## 4. Extended Physics Application: Ising Model Phase Transition

### Dataset: Synthetic (Simulated Ising Model)

**Source:** Standard Monte Carlo simulation.

**Contents:** 2D Ising model configurations at temperatures spanning the critical point.

**Mapping to framework:**
- **Observer interface:** Coarse-grained spin blocks at different block sizes.
- **Binding tensor:** Nearest-neighbor and block-averaged spin correlations.
- **Scale filtration:** Block size defines the scale parameter.
- **Transformation:** Temperature change drives the system through the phase transition.
- **Prediction:** At the critical temperature, coherence persists across all scales (scale invariance). Above the critical temperature, coherence drops at coarse scales but persists at fine scales. This maps directly to the framework's scale-existence theorem.

---

## Priority Ranking

| Priority | Dataset | Section | Effort | Impact |
|----------|---------|---------|--------|--------|
| 1 | OpenNeuro ds003171 (Anesthesia EEG) | Section 8 | Medium | High |
| 2 | Synthetic Gaussian | Section 7 | Low | Medium |
| 3 | Synthetic Ising Model | Extended | Medium | High |
| 4 | HCP Resting-State fMRI | Extended | High | High |
| 5 | OpenNeuro ds004148 (Propofol EEG) | Section 8 | Medium | Medium |
