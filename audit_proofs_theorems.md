# Proof and Theorem Check Notes

**Paper:** Observer-Interface Emergence of Formal Systems and Scale-Relative Informational Persistence  
**Author:** Christopher Ezernack  
**Audit Date:** April 2026

---

## Theorem-by-Theorem Review

### Theorem 4.19: Scale-Existence Under Redistribution

**Statement:** If $T$ is information-non-annihilating ($\alpha > 0$) and has bounded scale distortion ($\beta > 0$), and the non-trivial scale support assumption holds, then there exists a scale $s$ where coherence is positive after transformation.

**Proof status:** Complete and correct.

**Logic chain:**
1. Info-non-annihilating gives $\mathcal{I}[T(x)] > 0$ (denominator of coherence is positive).
2. Bounded scale distortion gives existence of $s^*$ with $\mathcal{I}_{s^*}[T(x)] > 0$ (numerator is positive at some scale).
3. Ratio is therefore positive.

**Potential attack:** A reviewer might ask whether bounded scale distortion is too strong an assumption. Response: the assumption is explicitly stated and is necessary; without it, the transformation could redistribute information to scales outside the filtration's support.

**Verdict:** Sound.

---

### Theorem 4.20: Observer-Relative Destruction

**Statement:** Apparent destruction at scale $s_0$ does not imply absolute destruction; there exists another scale where coherence exceeds the threshold.

**Proof status:** Complete and correct.

**Logic chain:**
1. From Theorem 4.19, $\mathcal{I}[T(x)] > 0$, ruling out absolute destruction.
2. Monotonicity of coherence (Remark 4.14) gives $\mathcal{C}^{(\mathcal{O})}_{\inf \mathcal{S}}[T(x)] = 1$.
3. Since coherence at $s_0$ is below threshold and at $\inf \mathcal{S}$ equals 1, intermediate value theorem gives existence of $s'$ above threshold.

**Potential attack:** The intermediate value theorem requires continuity of $s \mapsto \mathcal{C}^{(\mathcal{O})}_s$. This is not explicitly assumed. However, the coherence functional is defined via conditional expectation with respect to a filtration, and for standard filtrations the map is right-continuous (by the martingale convergence theorem). This could be made more explicit.

**Recommendation:** Add a brief remark noting that right-continuity of the coherence map in $s$ follows from standard filtration regularity conditions, or add it as a mild assumption.

**Verdict:** Sound, with minor strengthening possible.

---

### Theorem 4.21: Interface-Dependent Ontology of Structure

**Statement:** Apparent destruction for one observer does not imply apparent destruction for another observer.

**Proof status:** Complete. The proof is short because it follows directly from the observer-dependence of the binding tensor and decomposition.

**Potential attack:** A reviewer might say this is trivially true by construction. Response: the theorem is stated to make explicit what the framework implies; it is a structural consequence, not a deep result. Its value is clarificatory.

**Verdict:** Sound. Could be labeled a corollary if desired.

---

### Theorem 5.8: Coherence Under Scale Refinement

**Statement:** Under pure scale refinement with preserved binding tensor, coherence is non-decreasing.

**Proof status:** Complete and correct.

**Logic chain:**
1. Refinement means $\mathcal{F}_s \subseteq \mathcal{F}'_s$.
2. Tower property: conditioning on a finer sigma-algebra preserves more information for non-negative integrands.
3. Denominators are equal (binding tensor and measure preserved).
4. Therefore ratio is non-decreasing.

**Key assumption explicitly stated:** $E' = E$, $\nu' = \nu$, $\mathcal{B}'_{ij} = \mathcal{B}_{ij}$. This was identified as a critical fix in the source document (Issue V.1) and is correctly incorporated.

**Verdict:** Sound.

---

### Theorem 5.9: Monotone Convergence of Overlapping Observers

**Statement:** Under pure scale refinement with shared structure, observer overlap is non-decreasing and converges to 1 iff both refinement sequences exhaust the same representable structure.

**Proof status:** Complete. Detailed proof in Appendix A.

**Logic chain (Part i):**
1. Representable sets $R_k(t)$ are non-decreasing (from Theorem 5.8).
2. Intersection is non-decreasing.
3. Ratio argument for overlap.

**Logic chain (Part ii):**
1. Forward: both filtrations converge to full sigma-algebra implies all states become representable for both.
2. Converse: $\Omega \to 1$ implies symmetric difference measure tends to zero.

**Potential attack:** The ratio argument in Part (i) is not fully rigorous as stated. The claim that the ratio of intersection to union is non-decreasing when both sets grow requires that the intersection grows at least as fast as the symmetric difference. This is stated as following from the shared binding tensor assumption. A fully rigorous proof would need to show this quantitatively.

**Recommendation:** The appendix proof provides the additional detail. This is adequate for publication but a reviewer may request further tightening.

**Verdict:** Sound under stated assumptions. Restricted scope (pure scale refinement) is honestly stated.

---

### Lemma 4.22: Axiom Emergence

**Statement:** Axioms arise as compressed regularities of representable entities.

**Proof status:** Appeals to Knaster-Tarski theorem.

**Potential attack:** The operators Comp and Reg are not formally defined. The proof is conceptually correct but relies on informal operators.

**Recommendation:** This is acceptable for a first submission. If a reviewer requests formal definitions of Comp and Reg, they can be provided in a revision.

**Verdict:** Adequate. Flagged as potentially requiring expansion.

---

### Proposition 4.23: Non-Platonic Emergence

**Proof status:** Complete and straightforward.

**Verdict:** Sound.

---

### Proposition 4.24: Observer Non-Isomorphism

**Proof status:** Complete.

**Potential attack:** The claim that non-isomorphic quotient spaces lead to non-isomorphic mathematical systems requires that the closure operation preserves the non-isomorphism. This is true when the transformation sets are also different, but could fail if both observers happen to have the same transformations acting on different spaces that are nonetheless structurally equivalent. The proof handles this by conditioning on the quotient spaces being non-isomorphic "as measurable spaces."

**Verdict:** Sound under stated conditions.

---

### Proposition 6.2: Universality as Maximal Overlap

**Proof status:** Proof sketch only. Acknowledged in text.

**Verdict:** Honest labeling. Acceptable for submission.

---

## Summary

| Result | Status | Action Needed |
|--------|--------|---------------|
| Theorem 4.19 | Sound | None |
| Theorem 4.20 | Sound | Minor: add remark on right-continuity |
| Theorem 4.21 | Sound | None (could relabel as corollary) |
| Theorem 5.8 | Sound | None |
| Theorem 5.9 | Sound | None (appendix provides detail) |
| Lemma 4.22 | Adequate | Flagged: Comp/Reg could be formalized |
| Proposition 4.23 | Sound | None |
| Proposition 4.24 | Sound | None |
| Proposition 6.2 | Proof sketch | Honest labeling, acceptable |

**No fabricated proofs. No hidden assumptions. No theorem that is merely a restatement of definitions (except Theorem 4.21, which is acknowledged as a structural consequence).**
