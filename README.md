# Observer-Interface Emergence of Formal Systems and Scale-Relative Informational Persistence

**Author:** Christopher Ezernack

## Overview

This repository contains the complete manuscript, supporting materials, and reproducible figures for the paper *Observer-Interface Emergence of Formal Systems and Scale-Relative Informational Persistence*.

The paper establishes a formal framework in which mathematical systems and the apparent destruction of physical systems are treated as properties of an observer-scale-representation triple, rather than intrinsic properties of reality. Coherence, destruction, and persistence are all defined relative to an observer, a scale of observation, and a representation space.

## Repository Structure

```
creativity-model/
├── manuscript.tex              # Complete LaTeX manuscript
├── manuscript.pdf              # Compiled PDF (20 pages)
├── references.bib              # BibTeX bibliography
├── README.md                   # This file
├── figures/
│   ├── fig1_gaussian_coherence.py    # Simulation 1: Gaussian coherence
│   ├── fig1_gaussian_coherence.pdf   # Vector figure (PDF)
│   ├── fig1_gaussian_coherence.png   # Raster figure (PNG)
│   ├── fig2_neural_suppression.py    # Simulation 2: Neural suppression
│   ├── fig2_neural_suppression.pdf   # Vector figure (PDF)
│   ├── fig2_neural_suppression.png   # Raster figure (PNG)
│   ├── fig3_definition_chain.py      # Diagram: Definition dependency chain
│   ├── fig3_definition_chain.pdf     # Vector figure (PDF)
│   ├── fig3_definition_chain.png     # Raster figure (PNG)
│   ├── fig4_framework_comparison.py  # Radar chart: Framework comparison
│   ├── fig4_framework_comparison.pdf # Vector figure (PDF)
│   └── fig4_framework_comparison.png # Raster figure (PNG)
├── audit_notation_assumptions.md     # Notation and assumption audit
├── audit_citations.md                # Citation audit
├── audit_proofs_theorems.md          # Proof and theorem check notes
├── dataset_recommendations.md        # Recommended datasets for validation
└── simulation_plan.md                # Simulation plan for future work
```

## Building the Manuscript

```bash
pdflatex manuscript.tex
bibtex manuscript
pdflatex manuscript.tex
pdflatex manuscript.tex
```

## Reproducing Figures

All figures are generated with Python 3 and Matplotlib (no AI-generated images):

```bash
cd figures/
python3 fig1_gaussian_coherence.py
python3 fig2_neural_suppression.py
python3 fig3_definition_chain.py
python3 fig4_framework_comparison.py
```

## Key Contributions

1. **Observer-dependent coherence:** Coherence is defined as a functional of the observer interface, not an intrinsic property of the system.
2. **Scale-relative destruction:** Apparent destruction at one scale does not imply annihilation; informational structure persists at other scales.
3. **No fixed boundary:** The framework does not presuppose a fixed system boundary, inference architecture, or preferred basis.
4. **Mathematical emergence:** Formal systems emerge from the observer interface rather than being assumed as pre-existing Platonic objects.
5. **Framework unification:** IIT, FEP, and decoherence are recovered as special cases under additional assumptions.

## License

All rights reserved. Copyright Christopher Ezernack 2024-2026.
