
# 🧠 Cache Simulator with Replacement Policies

A configurable simulator for analyzing cache memory behavior using various replacement policies and cache configurations.

## 📁 Project Files

* `generate_trace.py` – Generates memory access traces with spatial and temporal locality.
* `cache_simulator.py` – Core simulator implementing LRU, FIFO, and Random replacement policies.
* `main.ipynb` – Runs multiple simulations, analyzes results, and generates visualizations.
* `example_trace.txt` – Example generated trace file.
* `results.csv` – Simulation result summary (hit/miss ratios).
* `/logs` – Directory storing logs for each configuration.

## 👨‍💻 Team Members

* Ethem Kesim – 210302205
* Emre Çubuk – 220302393
* Ozan Umut Güney – 200302109

---

## 🎯 Objective

Simulate different cache configurations and replacement policies to understand how:

* Cache size
* Block size
* Associativity
* Replacement policy
  affect cache performance (hit/miss ratios, cold/conflict misses).

---

## ⚙️ How It Works

### 1. Trace Generation (`generate_trace.py`)

Creates synthetic memory access traces with controllable locality.

### 2. Cache Simulation (`cache_simulator.py`)

Simulates cache operations based on:

* Configurable parameters
* Tracks cold/conflict misses
* Supports LRU, FIFO, and Random policies

### 3. Analysis and Visualization (`main.ipynb`)

Runs multiple configurations:

* 3 cache sizes: 16, 32, 64
* 3 associativities: 1, 2, 4
* 3 replacement policies: LRU, FIFO, Random
  Saves results to CSV and generates bar charts showing hit/miss ratios.

---

## 📊 Sample Results

* Larger cache → Higher hit ratio
* Higher associativity → Fewer conflict misses
* LRU outperforms FIFO/Random in most configurations

Visualization:

* Green bars = Hit ratio
* Red bars   = Miss ratio

---

## 🚧 Challenges

* **Trace randomness vs. consistency**: Balanced spatial/temporal locality while ensuring fair comparison.
* **File I/O and modularity**: Ensured clean integration between modules and notebook.

---

## ✅ Conclusion

The project successfully:

* Built a flexible cache simulator
* Quantified cold vs. conflict misses
* Compared replacement policies
* Visualized the performance impact of architectural choices

This tool can be extended to simulate multi-level caches and additional policies in the future.

---


