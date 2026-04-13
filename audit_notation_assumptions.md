# Notation and Assumption Audit

**Paper:** Observer-Interface Emergence of Formal Systems and Scale-Relative Informational Persistence  
**Author:** Christopher Ezernack  
**Audit Date:** April 13, 2026  
**Manuscript Version:** v2 (25 pages, 777 lines LaTeX, 0 compile errors, 0 warnings)

---

## 1. Symbol Consistency Check

| Symbol | Meaning | First Defined | Reused Elsewhere? | Status |
|--------|---------|---------------|-------------------|--------|
| $\mathcal{R}$ | Underlying reality | Def. 1 | No | Clean |
| $\mathcal{O}$ | Observer tuple | Def. 2 | No | Clean |
| $\mathcal{T}_{\mathcal{O}}$ | Admissible transformation set | Def. 3 | No | Clean |
| $I_{\mathcal{O}}$ | Interface map | Def. 4 | No | Clean |
| $\mathcal{R}_{\mathcal{O}}$ | Observer accessible quotient | Def. 5 | No | Clean |
| $\Sigma_{\mathcal{O}}$ | Observer state space | Def. 4 | No | Clean |
| $\{\mathcal{F}_s\}$ | Scale filtration | Def. 6 | No | Clean |
| $(E, \nu)$ | Component index space | Def. 7 | No | Clean |
| $\mathcal{B}_{ij}(x)$ | Binding tensor | Def. 8 | No | Clean |
| $\mathcal{I}[x]$ | Integrated relational information | Def. 9 | No | Clean |
| $\mathcal{I}_s[x]$ | Scale conditioned information | Def. 10 | No | Clean |
| $\mathcal{C}^{(\mathcal{O})}_s[x]$ | Coherence functional | Def. 11 | No | Clean |
| $\epsilon_{\mathcal{O}}$ | Coherence threshold | Def. 12 | No | Clean |
| $\mathcal{D}_{\mathcal{O}}$ | Distinction set | Def. 13 | No | Clean |
| $\mathcal{V}_{\mathcal{O}}$ | Invariant set | Def. 14 | No | Clean |
| $\mathfrak{M}_{\mathcal{O}}$ | Observer relative formal system | Def. 15 | No | Clean |
| $\Psi_{\mathcal{O}}$ | Representability map | Def. 16 | No | Clean |
| $\alpha$ | Info non-annihilation parameter | Def. 17 | No | **Reserved** |
| $\beta$ | Bounded scale distortion parameter | Def. 18 | No | **Reserved** |
| $\gamma$ | Neural suppression parameter | Example 2 | No | **Reserved** |
| $\mathcal{J}(\mathcal{O}_1, \mathcal{O}_2)$ | Joint representability set | Def. 19 | No | Clean |
| $\mathfrak{M}_{\mathcal{O}_1 \cap \mathcal{O}_2}$ | Shared formal system | Def. 20 | No | Clean |
| $\Omega(\mathcal{O}_1, \mathcal{O}_2)$ | Observer overlap | Def. 24 | No | Clean |
| $\Xi$ | Observer evolution map | Def. 25 | No | Clean |
| $\Delta\Psi$ | Representability expansion | Def. 26 | No | Clean |
| $\nabla\Psi$ | Representability contraction | Def. 27 | No | Clean |

**Result:** No symbol reuse detected. All reserved parameters ($\alpha$, $\beta$, $\gamma$) are used exclusively for their designated purposes. $\epsilon_{\mathcal{O}}$ is used only as the coherence threshold.

---

## 2. Dash Audit

No em-dashes or en-dashes found in prose text. Mathematical minus signs in equations are correctly formatted LaTeX.

---

## 3. Assumption Tracking

| Assumption | Where Introduced | Where Used | Explicitly Stated? | Status |
|-----------|-----------------|------------|-------------------|--------|
| $\mathcal{R}$ is measurable | Def. 1 | All | Yes | Clean |
| $I_{\mathcal{O}}$ is measurable | Def. 4 | All downstream | Yes | Clean |
| $\mathcal{B}_{ij}(x) \geq 0$ | Def. 8 | Defs. 9-11, all theorems | Yes | Clean |
| $\nu$ is finite measure | Def. 7 | Def. 9 integral | Yes | Clean |
| Non-Trivial Scale Support | Assumption 1 | Theorem 2 | Yes, named | Clean |
| $T$ is $\alpha$-non-annihilating | Def. 17 | Theorem 1 | Yes | Clean |
| $T$ has bounded scale distortion | Def. 18 | Theorem 2 | Yes | Clean |
| Mutual non-singularity | Def. 21 | Theorems 4, 5 | Yes | Clean |
| Compatible filtrations | Def. 23 | Theorem 5 | Yes | Clean |
| Pure scale refinement | Thm. 7 hypothesis | Theorem 8 | Yes | Clean |
| $E' = E, \nu' = \nu, \mathcal{B}' = \mathcal{B}$ | Thm. 7 hypothesis | Theorem 7 | Yes | Clean |

**Result:** No hidden assumptions detected. Every assumption used in a theorem is explicitly stated in the theorem hypotheses or in a preceding named Assumption.

---

## 4. Hidden Assumption Flags

1. **Theorem 3 (Observer Relative Destruction):** Uses monotonicity of coherence in $s$. Justified in Appendix A.4. Depends on non-negativity of binding tensor (Def. 8). Chain is complete; no hidden assumption.

2. **Theorem 4 (Interface Dependent Ontology):** Follows by construction from the observer parameterization. Could be downgraded to a proposition if a reviewer objects that it is definitional rather than substantive. Currently labeled as a theorem for structural emphasis.

3. **Theorem 5 (Emergent Universality), part (iv):** Invokes Knaster-Tarski for the intersection lattice. Valid because the power set of $\Sigma_{\mathcal{O}}$ is a complete lattice under inclusion. No hidden assumption.

4. **Theorem 7 (Monotonic Expansion under Refinement):** The hypothesis explicitly requires $E' = E$, $\nu' = \nu$, and $\mathcal{B}'_{ij} = \mathcal{B}_{ij}$. Without these, the theorem fails. These are stated, not hidden.

5. **Theorem 8 (Monotone Convergence):** Restricted to pure scale refinement with shared $\mathcal{R}, E, \nu, \mathcal{B}, \mathcal{T}_{\mathcal{O}}$. General case flagged as future work (Remark after Theorem 8). No hidden assumption.

---

## 5. Formal Object Count

| Type | Count | Expected from PDF | Status |
|------|-------|-------------------|--------|
| Definitions | 29 | 29 | PASS |
| Lemmas | 1 | 1 | PASS |
| Propositions | 2 | 2 | PASS |
| Theorems | 8 | 8 | PASS |
| Corollaries | 1 | 1 | PASS |
| Assumptions | 1 | 1 | PASS |
| Remarks | 8 | variable | PASS |

---

## 6. Definition Dependency Chain

The following chain must remain intact for the theorems to hold:

$$\mathcal{R} \to \mathcal{O} \to I_{\mathcal{O}} \to \Sigma_{\mathcal{O}} \to (E, \nu) \to \mathcal{B}_{ij} \to \mathcal{I}[x] \to \{\mathcal{F}_s\} \to \mathcal{I}_s[x] \to \mathcal{C}^{(\mathcal{O})}_s \to \mathcal{D}_{\mathcal{O}} \to \mathcal{V}_{\mathcal{O}} \to \mathfrak{M}_{\mathcal{O}} \to \Psi_{\mathcal{O}}$$

No definition in this chain can be removed or reordered without breaking the downstream theorems.

---

## 7. Overall Assessment

The notation is globally consistent. All assumptions are stated before use. No hidden monotonicity assumptions detected. The reserved parameters ($\alpha$, $\beta$, $\gamma$, $\epsilon_{\mathcal{O}}$) are used exclusively as specified. The definition dependency chain is intact and correctly ordered in the manuscript.
