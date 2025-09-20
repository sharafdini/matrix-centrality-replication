
# Replication of Centrality Experiments in  
**"Centrality Measures Based on Matrix Functions" (Njotto, 2018)**

This repository contains Python code used by my **master’s degree student** as part of her thesis work.  
She attempted to **replicate and verify** the numerical experiments reported in:

> Njotto (2018), *Centrality Measures Based on Matrix Functions*,  
> Open Journal of Discrete Mathematics, Vol. 08 No. 03, pp. 93–118.  
> DOI: [10.4236/ojdm.2018.83006](https://doi.org/10.4236/ojdm.2018.83006)

---

## 🎯 Purpose

As part of her thesis, my student carefully studied the article and tried to reproduce the Kendall correlation results reported in **Table 7** (Barabási–Albert networks) and **Table 9** (Erdős–Rényi networks).

- The original paper reports that for generalized Katz centralities (\(k_3\) and \(k_4\)), the Kendall coefficient \(\tau_{k_3,k_4}\) is **always 1.0**.  
- Our replication attempts using different plausible definitions of “absolute value of the inverse function” (entrywise absolute, spectral absolute, vector absolute) did **not** reproduce this result. Instead, values were near zero or negative.  

This repository documents the replication code so that other researchers (and the original author) can inspect, reproduce, and clarify the computational details.

---

## 📂 Repository Structure

- **`replicate_table7.py`**  
  Reproduces Table 7 for BA(\(n=200, m\)) networks.  
  - Implements Katz variants \(k_1,\dots,k_4\).  
  - Compares Kendall’s \(\tau\) across pairs.  
  - Tests three interpretations of “absolute value of the inverse function.”  
  - Outputs averaged Kendall coefficients for \(m \in \{1,2,3,5,6,7,8,10,15,40\}\).

- **`replicate_table9.py`**  
  Reproduces Table 9 for ER(\(n=200, p\)) networks.  
  - Implements Katz variants \(k_1,\dots,k_4\).  
  - Computes Kendall coefficients: \(\tau(k_1,k_2), \tau(k_1,k_3), \tau(k_2,k_3), \tau(k_3,k_4)\).  
  - Uses absolute-inverse handling for \(k_3,k_4\).  
  - Outputs results for several values of \(p\).


- **`README.md`**  
  This file.

---

## ⚙️ Requirements

- Python ≥ 3.9  
- Packages: `numpy`, `scipy`, `networkx`, `pandas`

Install with:

```bash
pip install numpy scipy networkx pandas
