# Notation and Assumption Audit

**Paper:** Observer-Interface Emergence of Formal Systems and Scale-Relative Informational Persistence  
**Author:** Christopher Ezernack  
**Audit Date:** April 2026

---

## 1. Symbol Consistency Check

| Symbol | Meaning | First Defined | Reused Elsewhere? | Status |
|--------|---------|---------------|-------------------|--------|
| $\mathcal{R}$ | Underlying reality | Definition 4.1 | No | Clean |
| $\mathcal{O}$ | Observer class tuple | Definition 4.2 | No | Clean |
| $I_{\mathcal{O}}$ | Interface map | Definition 4.2 | No | Clean |
| $\Sigma_{\mathcal{O}}$ | Observer state space | Definition 4.2 | No | Clean |
| $E, \nu$ | Index space, measure | Definition 4.8 | No | Clean |
| $\mathcal{B}_{ij}$ | Binding tensor | Definition 4.9 | No | Clean |
| $\mathcal{I}[x]$ | Integrated relational info | Definition 4.10 | No | Clean |
| $\mathcal{I}_s[x]$ | Scale-conditioned info | Definition 4.12 | No | Clean |
| $\mathcal{C}^{(\mathcal{O})}_s$ | Coherence functional | Definition 4.13 | No | Clean |
| $\{\mathcal{F}_s\}$ | Scale filtration | Definition 4.11 | No | Clean |
| $\mathcal{T}_{\mathcal{O}}$ | Admissible transformations | Definition 4.3 | No | Clean |
| $\mathcal{D}_{\mathcal{O}}$ | Distinction set | Definition 4.5 | No | Clean |
| $\mathcal{V}_{\mathcal{O}}$ | Invariant set | Definition 4.6 | No | Clean |
| $\mathfrak{M}_{\mathcal{O}}$ | Induced math system | Definition 4.7 | No | Clean |
| $\Psi_{\mathcal{O}}$ | Representability map | Definition 4.14 | No | Clean |
| $\epsilon_{\mathcal{O}}$ | Detection threshold | Definition 4.14 | No | Clean |
| $\alpha$ | Info non-annihilation param | Definition 4.15 | No | **Reserved** |
| $\beta$ | Bounded scale distortion | Definition 4.16 | No | **Reserved** |
| $\gamma$ | Neural suppression param | Example 8.1 | No | **Reserved** |
| $\Omega$ | Observer overlap | Definition 5.7 | No | Clean |
| $\Delta\Psi$ | Perceptual expansion | Definition 5.2 | No | Clean |
| $\nabla\Psi$ | Perceptual contraction | Definition 5.3 | No | Clean |
| $\Xi$ | Observer evolution map | Definition 5.1 | No | Clean |

**Result:** No symbol reuse detected. All reserved parameters ($\alpha$, $\beta$, $\gamma$) are used only for their designated purposes.

---

## 2. Assumption Audit

| Assumption | Location | Used By | Explicitly Stated? | Status |
|-----------|----------|---------|-------------------|--------|
| $\mathcal{R}$ is measurable topological | Def 4.1 | All | Yes | Clean |
| $I_{\mathcal{O}}$ is measurable | Def 4.2 | Def 4.4, Props | Yes | Clean |
| Decomposition exists | Def 4.8 | Def 4.9 onward | Yes, with caveat | Clean |
| $\mathcal{B}_{ij} \geq 0$ | Def 4.9 | Def 4.10, all theorems | Yes | Clean |
| $\nu$ is $\sigma$-finite | Def 4.8 | Def 4.10 integral | Yes | Clean |
| Filtration is non-degenerate | Assumption 4.18 | Thm 4.19, 4.20 | Yes | Clean |
| $T$ is info-non-annihilating | Def 4.15 | Thm 4.19, 4.20 | Yes | Clean |
| $T$ has bounded scale distortion | Def 4.16 | Thm 4.19 | Yes | Clean |
| Binding tensor preserved under refinement | Thm 5.8 | Thm 5.9 | Yes | Clean |
| Mutual non-singularity preserved | Thm 5.9 | Thm 5.9 | Yes | Clean |

**Result:** No hidden assumptions detected. Every assumption used in a theorem is explicitly stated in the theorem's hypotheses or in a preceding named Assumption.

---

## 3. Potential Weak Points (Flagged for Awareness)

1. **Theorem 4.21 (Interface-Dependent Ontology):** This is more of a corollary of the framework's definitions than a deep theorem. It follows directly from the observer-dependence of the binding tensor. Labeled as a theorem for structural emphasis, but could be downgraded to a proposition if a reviewer objects.

2. **Lemma 4.22 (Axiom Emergence):** The operators Comp and Reg are described informally. A fully rigorous treatment would require specifying the lattice structure and the compression criterion. The proof appeals to the Knaster-Tarski theorem, which is valid but the mapping to the specific lattice could be made more explicit.

3. **Proposition 6.2 (Universality):** This is labeled as a proof sketch. The claim that the framework's own tools belong to the overlap of all sufficiently structured observer systems is plausible but not formally proved. This is acknowledged in the text.

4. **Monotonicity of coherence (Remark 4.14):** The argument uses Jensen's inequality on conditional expectations. This is correct for non-negative integrands but requires the conditional expectation to be well-defined, which it is under the $\sigma$-finiteness assumption on $\nu$.

---

## 4. Definition Dependency Chain

The following chain must remain intact for the theorems to hold:

$$\mathcal{R} \to \mathcal{O} \to I_{\mathcal{O}} \to \Sigma_{\mathcal{O}} \to (E, \nu) \to \mathcal{B}_{ij} \to \mathcal{I}[x] \to \{\mathcal{F}_s\} \to \mathcal{I}_s[x] \to \mathcal{C}^{(\mathcal{O})}_s \to \Psi_{\mathcal{O}}$$

No definition in this chain can be removed or reordered without breaking the downstream theorems.
