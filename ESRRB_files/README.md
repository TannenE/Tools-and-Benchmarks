# ESRRB Files — Model Development Overview

This directory contains RE:IN models developed to study pluripotency, formative transition, and the role of **ESRRB**.  
Folders are ordered below according to the **actual flow of the research**.

---

## Maintained_notmaintained_early
Initial models based on **serum + LIF** conditions and the **original 23 experiments**, with additional single-gene knockouts.
Used to learn how to translate published experimental setups into RE:IN-compatible models and to explore early KO behavior.

---

## 717_modelchecks_jan2022
Early large-scale exploration of **717-constrained models** .
Includes models with genes and interactions to identify which interaction sets admit solutions.
Some models include activators and test large batches of interaction configurations.
The most up to date model ends with 106.rein and includes the following genes and experiments:Lif,CH,PD,Stat3,Tcf3,MEKERK,Klf4,Gbx2,TFcp2l1, ESRRB,
Nanog,Klf2,Tbx3,Sox2,Sall4,Oct4,DNmt3a,Dnmt3b,Utf1,Otx2,Etv5,Etv4,Nr0b1,Zic3,Lef1,Tcf15.
All 23 experiments




---

## New_models_with_formative_6_jan31
Introduction of **formative genes and formative transition experiments**.
Built from Pearson ≥ 0.5 interactions, with selective use of activators.
Each new experiment was tested individually before combining them into unified models.
Genes that continued to have activators: Stat3, Klf4, Gbx2 , Tfccp2l1 , Esrrb, Nanog, Klf2, Tbx3, Sox2, Sall4, Oct4.
Also, all of the Formative genes lost their -+ except for those who were knocked out

---

## all_9_experiments_march10
Zic3 and Etv4 were removed from the files. 3 new experiments were added: 96 hours and not 2il , 96 hours esrrb over expression→ 2il And 2ilesrrbKO → 2ilesrrb48hoursKO bringing the total to 9. 
With these 9 formative experiments, I ran each one individually as well as all of them together. 

Models incorporating **9 formative experiments**
- ESRRB overexpression
- ESRRB knockout
- 96-hour transition experiments

---

## testing_timestamps
Focused on **temporal dynamics** and gene state transitions.
Includes timestamp-specific experiments (e.g. `Utf1_1_8`,1=on timetsmap 8) to determine when genes change state.
Also has checks on oct4 and sox2 specifically. Sometimes alone and sometimes with the original 23 experiments

---

## no_oscillation_testing
Genes at this point include, all pluripotent+ Dnmt3a,Dnmt3b,Utf1,Otx2,Etv5,Nr0b1,Lef1,Tcf15,Oct6,Rbjp
Models addressing **oscillatory behavior** observed in earlier phases.
Genes such as *Rbjp, Oct6, Nr0b1* were removed in some variants.
Experiments were reduced to a minimal essential subset to identify stable, non-oscillatory configurations.

---

## true_false_testing
Validation of **true/false gene predictions** under controlled conditions.
Includes variation of timestamps (5, 10, 15, etc.) and constraints to suppress oscillations.
Primarily checks pluripotency gene behavior at 48 hours.

---

---

## Pearson_correlation_findings
Systematic testing of interactions derived from **Pearson correlation thresholds**.
Used to identify essential interactions and determine the minimal correlation value that still produces valid models.
Key interactions (e.g. *Esrrb–Utf1, Lef1–Dnmt3b*) were validated through repeated testing and correspondence.

---

## Finding_min_model
Final phase focused on identifying a **minimal ESRRB-centered model**.
Contains reduced gene sets and interactions that preserve correct behavior without oscillations.
Represents the endpoint of the model-refinement pipeline.

---

## Notes
Artilce_File is the file used in the article:
Carbognin, E., Carlini, V., Panariello, F. et al. Esrrb guides naive pluripotent cells through the formative transcriptional programme. Nat Cell Biol 25, 643–657 (2023). https://doi.org/10.1038/s41556-023-01131-x
Please refer there for further information regarding this reserach 
