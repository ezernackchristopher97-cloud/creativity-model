# Proof and Theorem Check Notes

**Paper:** Observer-Interface Emergence of Formal Systems and Scale-Relative Informational Persistence  
**Author:** Christopher Ezernack  
**Audit Date:** April 13, 2026  
**Manuscript Version:** v2 (25 pages, 8 theorems, 1 lemma, 2 propositions, 1 corollary)

---

## Theorem-by-Theorem Review

### Lemma 1: Scale Decomposition via Chain Rule

**Statement:** For any $s_1 \leq s_2$, the scale conditioned information decomposes as a sum of the coarser-scale information plus the information lost between scales.

**Proof method:** Tower property of conditional expectation + linearity of integration.

**Assessment:** Correct. The proof is a direct application of standard measure theory. The tower property is invoked correctly. No hidden assumptions.

**Status:** PASS

---

### Proposition 1: Non-Isomorphism of Observer Relative Formal Systems

**Statement:** For observers with distinct interface maps, the formal systems are in general non-isomorphic.

**Assessment:** Structural observation. Follows from the fact that different interface maps produce different equivalence classes on $\mathcal{R}$. The "in general" qualifier is appropriate. Correctly labeled as a proposition.

**Status:** PASS

---

### Proposition 2: Cross-Observer Intersection

**Statement:** For observers interacting with the same $\mathcal{R}$, the intersection of their formal systems is non-empty under mild conditions.

**Assessment:** Preview of Theorem 5. The "mild conditions" are made precise in Definition 21 (mutual non-singularity). Correctly labeled as a proposition.

**Status:** PASS

---

### Theorem 1: Scale Existence Under Redistribution

**Statement:** If $\mathcal{I}[x] > 0$ and $T$ is $\alpha$-non-annihilating, then there exists $s$ such that $\mathcal{C}_s^{(\mathcal{O})}[T(x)] > 0$.

**Proof method:** Chain from $\alpha$-non-annihilation to positivity of total information, then evaluation at finest scale $s_{\min}$.

**Assessment:** Correct but deliberately weak. The proof shows existence at $s_{\min}$ where coherence equals 1. The Remark following the theorem explicitly acknowledges that this result is "too easy" and motivates Theorem 2.

**Potential weakness:** Essentially a restatement of definitions. A reviewer could argue this is not a theorem. The paper pre-empts this by immediately presenting the strengthened version (Theorem 2).

**Status:** PASS (weakness acknowledged in paper)

---

### Theorem 2: Nontrivial Scale Persistence (Strengthened)

**Statement:** Under the Non-Trivial Scale Support Condition and bounded scale distortion with parameter $\beta > 0$, there exists $s^*$ such that $\mathcal{C}_{s^*}^{(\mathcal{O})}[T(x)] \geq \beta \cdot \mathcal{I}_{s^*}[x] / \mathcal{I}[T(x)] > 0$.

**Proof method:** Direct substitution of the bounded scale distortion inequality into the coherence ratio.

**Assessment:** Correct. The quantitative lower bound is non-trivial. The Non-Trivial Scale Support Condition (Assumption 1) is explicitly stated before the theorem.

**Status:** PASS

---

### Theorem 3: Observer Relative Destruction

**Statement:** If coherence falls below $\epsilon_{\mathcal{O}}$ at coarse scale $s_0$, the state is apparently destroyed. But if $\mathcal{I}[x] > 0$, there exists finer scale $s' < s_0$ where coherence exceeds $\epsilon_{\mathcal{O}}$.

**Proof method:** Monotonicity of coherence in $s$ (non-increasing) + boundary values at $s_{\min}$ and $s_0$.

**Assessment:** Correct. The monotonicity claim is justified in Appendix A.4. The argument does not require continuity; it uses only monotonicity and boundary values. The proof explicitly states: "This requires no continuity assumption and no complex measurability argument; it is a direct consequence of the filtration structure."

**Status:** PASS

---

### Theorem 4: Interface Dependent Ontology

**Statement:** The formal system, distinction set, and representability map are all determined by the observer tuple.

**Proof method:** Construction (each object is parameterized by the observer tuple).

**Assessment:** Definitional. Follows directly from the parameterization. Could be downgraded to a proposition. Currently labeled as a theorem for structural emphasis.

**Potential weakness:** A reviewer may argue this is trivially true by construction.

**Status:** PASS (with caveat)

---

### Theorem 5: Structured Intersection

**Statement:** Under mutual non-singularity: (i) joint representability set is non-empty with positive measure, (ii) shared formal system is non-empty, (iii) closed under shared transformations, (iv) is itself a formal system.

**Proof method:** (i) Measure-theoretic from mutual non-singularity. (ii) Existence from (i). (iii) Set-theoretic closure. (iv) Knaster-Tarski on intersection lattice.

**Assessment:** Correct. Part (iv) requires the intersection to form a complete lattice, which holds because the power set is a complete lattice under inclusion.

**Status:** PASS

---

### Theorem 6: Emergent Universality

**Statement:** For a finite pairwise non-singular family with compatible filtrations: (i) global intersection $\mathfrak{M}^*$ is non-empty, (ii) closed under shared transformations, (iii) stable under addition of new observers, (iv) determined by $\mathcal{R}$.

**Proof method:** (i) Induction on $|K|$ using Theorem 5. (ii) Set-theoretic closure. (iii) Subset argument. (iv) Intersection filters out observer-specific artifacts.

**Assessment:** Correct for finite families. Finiteness of $K$ is essential and explicitly noted in the Remark following the theorem.

**Potential weakness:** Part (iv) is more interpretive than mathematical. The claim that observer-specific artifacts are filtered out is plausible but not formally proved in the strict sense.

**Status:** PASS (with caveat on part (iv))

---

### Theorem 7: Monotonic Expansion under Refinement

**Statement:** Under pure scale refinement with preserved $E, \nu, \mathcal{B}$, the formal system expands: $\mathfrak{M}_{\mathcal{O}} \subseteq \mathfrak{M}_{\mathcal{O}'}$.

**Proof method:** Tower property shows $\mathcal{I}_s'[x] \geq \mathcal{I}_s[x]$. With preserved total information, coherence increases. Expanding transformation set preserves closure.

**Assessment:** Correct. The hypothesis is strong but explicitly stated. Without these conditions, the theorem would fail.

**Status:** PASS

---

### Theorem 8: Monotone Convergence of Overlapping Observers under Scale Refinement

**Statement:** Under pure scale refinement with shared $\mathcal{R}, E, \nu, \mathcal{B}, \mathcal{T}_{\mathcal{O}}$: (i) overlap $\Omega$ is non-decreasing, (ii) $\Omega \to 1$ iff both sequences exhaust the same representable structure.

**Proof method:** (i) Monotonicity from Theorem 7 + expanding formal systems. (ii) Characterization of the limit.

**Assessment:** Correct under stated hypotheses. General case flagged as future work.

**Status:** PASS

---

### Corollary 1: Non-Platonic Convergence

**Statement:** Apparent universality of mathematics does not require Platonic objects; it follows from shared reality and mutual non-singularity.

**Assessment:** Philosophical interpretation of Theorem 6. Correctly labeled as a corollary.

**Status:** PASS

---

## Summary

| Result | Status | Notes |
|--------|--------|-------|
| Lemma 1 | PASS | Standard measure theory |
| Proposition 1 | PASS | Structural observation |
| Proposition 2 | PASS | Preview of Theorem 5 |
| Theorem 1 | PASS | Deliberately weak; motivates Theorem 2 |
| Theorem 2 | PASS | Strengthened with quantitative bound |
| Theorem 3 | PASS | Monotonicity justified in appendix |
| Theorem 4 | PASS | Definitional; could be downgraded |
| Theorem 5 | PASS | Knaster-Tarski valid |
| Theorem 6 | PASS | Finite families only; part (iv) interpretive |
| Theorem 7 | PASS | Strong hypothesis explicitly stated |
| Theorem 8 | PASS | Restricted to pure scale refinement |
| Corollary 1 | PASS | Philosophical interpretation |

**Overall:** All proofs are logically valid under their stated hypotheses. No circular reasoning detected. No hidden assumptions. No fabricated proofs. Weak points are acknowledged in the paper itself.
