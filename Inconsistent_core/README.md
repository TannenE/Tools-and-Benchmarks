# Inconsistent Core (ICC) Algorithm

The **Inconsistent Core (ICC)** algorithm is designed to improve the usability of the RE:IN and BREIN tools by helping users *diagnose why a model has no solutions*.  
Instead of returning a generic **“no solutions found”**, ICC identifies *which experiments or constraints are responsible for the inconsistency*.

---

## Motivation

When working with large `.rein` files, it is common for inconsistencies to arise from:
- Conflicting experiments
- Over-constrained models
- Incorrect experimental assumptions

RE:IN will only give you solutions found or no solutions found.  
The ICC algorithm seeks to add an **explainability layer**, allowing users to pinpoint *where* the inconsistency originates.

---

## Core Concept

Given a set of experiments that yields **no solutions**, ICC finds a **minimal inconsistent core**:

- The full set of experiments has **no solutions**
- Removing *any single experiment* from the core restores **solutions**

This allows users to:
- Identify problematic experiments
- Debug experimental assumptions
- Refine models incrementally

> **Note:** The algorithm finds a *minimal* inconsistent set, not necessarily the *smallest* possible one.

---

## How the Algorithm Works

### 1. Parse the `.rein` File
- Experiments are detected using `#Experiment` markers
- Commented lines (`//`) are ignored
- Experiments are indexed and stored for iterative testing

---

### 2. Iterative Experiment Removal

For each experiment:
1. Temporarily remove the experiment from the file
2. Run RE:IN on the modified file
3. Observe the result:
   - **Solutions found** → the experiment is **essential** and kept
   - **No solutions** → the experiment is removed permanently

This process progressively shrinks the experiment set.

---

### 3. Recursive Reduction

The algorithm continues iterating through the remaining experiments until:
- All remaining experiments are mutually inconsistent, or
- Only one experiment remains

If a single experiment still produces no solutions, the inconsistency likely arises from **interaction definitions**, not experiments.

---

### 4. Termination and Output

The final output is:
- A **minimal inconsistent core** of experiments, or
- A single experiment indicating a self-contained inconsistency, or
- An indication that the issue lies outside experimental constraints

---

## Modes of Operation

### Experiment-Level Broad Search 1
- Removes entire experiments at once
- Best for identifying conflicting experimental constraints

### Line-Level Fine Search 2
- Intended to remove individual constraint blocks
- Defined in the code but not fully implemented

---

## Implementation Notes

- Temporary `.rein` files are generated during execution
- A `curFile.txt` pointer is used to indicate the active file for RE:IN
- RE:IN is executed via Jupyter using `nbconvert`
- The algorithm is **order-dependent**; different experiment orders may yield different cores

---

## Practical Use

The ICC algorithm is particularly useful when:
- Working with large experimental datasets
- Translating biological experiments into RE:IN constraints
- Debugging newly added experiments
- Teaching or demonstrating model inconsistency

---

---

## How to Run
- Enter the path that the requested file is found
- python3 ICC_algorithm.py
- path to file
- run



---
## Summary

The Inconsistent Core algorithm attempts to provide a practical, model-driven way to:
- Identify the source of inconsistencies
- Improve feedback from RE:IN 
- Make large regulatory models easier to debug and maintain

This is a prelimmary algorithm but does work effectivley in the test file also attached to this folder.

