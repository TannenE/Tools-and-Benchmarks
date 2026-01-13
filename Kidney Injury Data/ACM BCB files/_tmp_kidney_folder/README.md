# Reasoning‑about‑GRN‑Ensembles‑in‑Kidney‑Injury‑and‑Repair

**Characterizing Gene Regulatory Network Ensembles in Kidney Injury and Repair**  
A computational framework using RE:IN to infer and analyze ensembles of Boolean gene regulatory networks (GRNs) from single-cell RNA‑seq data in a mouse model of acute kidney injury.

---

## Project Motivation & Highlights

This work addresses the challenge that multiple GRNs can explain the same transcriptional data. By leveraging the **Reasoning Engine for Interaction Networks (RE:IN)**, we:

1. Inferred language-level Abstract Boolean Networks (ABN) for proximal tubule cell states in ischemia‑reperfusion injury.  
2. Generated  ensembles of GRN solutions consistent with observed expression patterns.  
3. Applied PCA to reveal four distinct GRN families.  
4. Identified key subnetwork structures differentiating those families.  

The resulting methodology enhances our understanding of GRN heterogeneity during kidney injury and repair 

---

## Repository Contents

- **`dataset_C_for_git.rein`**, `bulk_data_boolean.csv`, `Data_set_c.csv`, `cluster_samples*.csv` – Inputs and processed data for ABN and Boolean network modeling.  
- **`Table S1 - pseudo-bulk counts.xlsx`** – Aggregated single-cell data.  
- **`README.md`** – This file.  
- **Other files** – Intermediate data dumps and computational artifacts.

---

## 🔧 Getting Started

### 1. Requirements

- `RE:IN` tool from [fsprojects/ReasoningEngine](https://github.com/fsprojects/ReasoningEngine)

### 2. Setup

```bash
git clone https://github.com/TannenE/Reasoning-about-Gene-Regulatory-Network-Ensembles-in-Kidney-Injury-and-Repair.git
cd Reasoning-about-Gene-Regulatory-Network-Ensembles-in-Kidney-Injury-and-Repair
