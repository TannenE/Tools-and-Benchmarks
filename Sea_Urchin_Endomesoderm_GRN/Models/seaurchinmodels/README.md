# Sea Urchin Endomesoderm GRN Models

This directory contains RE:IN-compatible gene regulatory network (GRN) models and experiments related to **sea urchin endomesoderm specification**.  
The contents reflect a progression from published experimental figures to exploratory and domain-divided model analyses used in subsequent methodological work.

---

## Figure-based Models (PNAS)

The folders labeled by figure (e.g. *Figure A*, *Figure C*, *Figure D*, *Figure E*, *Figure F*) are direct adaptations of experimental conditions and perturbations described in:

> Peter et al., *“A gene regulatory network controlling the initiation of endomesoderm specification in the sea urchin embryo”*  
> **PNAS (2017)**  
> https://www.pnas.org/doi/10.1073/pnas.1610616114

These folders encode the **overexpression and knockout experiments** presented in **Figure 1** and related figures of the paper, translated into RE:IN-friendly formats.  
They serve as a biological grounding and validation baseline as well as testing run-time, constraints and experiments 

Folders include:
- `Figure A Overexpressions`
- `Figure C knockouts`
- `Figure C overexpressions`
- `Figure D knockouts`
- `Figure E knockouts`
- `Figure E overexpressions`
- `Figure F knockouts`
- `Figure F overexpressions`

---

## Search-Inferred and KO / FE Models

Folders such as:
- `SearchinmodelsFig1`
- `SearchinmodelsKO+FE_1A`
- `SearchinmodelsKO+FE_1C`
- `SearchinmodelsKO+FE_1D`
- `SearchinmodelsKO+FE_1F`

contain **search-derived GRN ensembles**, including combinations of knockouts (KO) and formative/endomesoderm (FE) constraints.  
These models were generated using the RE:IN tooling to explore alternative network structures consistent with the figure-based experimental data.

---

## Domain-Divided Models (DDM)

The folders:
- `DDM_QFE`
- `DDM_8FE`
- `DDM_8KO`
- `DDM_TKO`
- `60-119`

contain **domain-divided models**, where the GRN is partitioned into functional or experimental domains to enable systematic analysis of constraint interactions, perturbations, and solution spaces.

These models were used in conjunction with the tools provided in the broader repository and formed part of the experimental analysis described in:

> *“Formal Reasoning over Ensembles of Gene Regulatory Networks”*  
> Springer, LNCS  
> https://link.springer.com/chapter/10.1007/978-3-031-89704-7_4

---

## Full Genome and Bonus Experiments

- `Full_Genome_Bonus`
- `Experiment_19`

These folders contain additional or extended experiments, including larger genome-scale configurations and supplementary analyses that go beyond the core figure-based models.  
They were used for stress-testing the RE:IN framework and exploring model scalability and robustness.

---

  
