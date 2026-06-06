Markdown
<p align="center">
  <img src="logo.png" alt="fasthardware Official Logo" width="400">
</p>
# ⚡ fasthardware

[![PyPI version](https://img.shields.io/pypi/v/fasthardware.svg)](https://pypi.org/project/fasthardware/)
[![Downloads](https://pepy.tech/badge/fasthardware)](https://pepy.tech/project/fasthardware)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Maximize the absolute computing power of your Python process and all its child processes with just a single line of code.**

`fasthardware` is a lightweight, zero-configuration hardware acceleration injector designed for high-performance, real-time Python applications (e.g., YOLO object detection, MediaPipe pose estimation, OpenCV video pipelines, and heavy distributed inference loops).

By hijacking the OS scheduler, managing runtime memory thresholds, and forcing strict CPU core binding across multi-processes, `fasthardware` eliminates micro-stuttering and stabilizes frames under heavy loads.

---

## 🚀 Key Features

* **OS Priority Escalation:** Automatically forces the host OS (Windows/Linux) to allocate maximum CPU scheduling priority to your Python process.
* **🔥 ULTIMATE Multi-Process Interception:** Automatically tracks all spawned child processes, forces them into high-priority classes, and binds them to dedicated CPU cores (`CPU Affinity`) to eliminate distributed bottlenecks.
* **Micro-Stuttering Elimination:** Optimizes Python's Garbage Collection (GC) thresholds to prevent "Stop-the-World" latency spikes during heavy loops.
* **C-Level Multicore Mobilization:** Injects global environment flags (`OMP`, `MKL`, `OPENBLAS`, `NUMEXPR`) to force underlying C/C++ backed libraries (NumPy, OpenCV) to utilize every single logical core available.
* **Zero-Config Integration:** No code rewrites. Just import it at the very top of your script.

---

## 📦 Installation

Install the package directly from PyPI:

```bash
pip install fasthardware
```
🛠️ Quick Start
1. Default Mode (Single Process Boost)
Perfect for standard loops like standalone YOLO inference or single-camera stream pipelines.

```Python
from fasthardware import fasthardware
```

# Unlock maximum priority for the current process
```Python
fasthardware.speedup()
```

# Your heavy real-time loop goes here...
2. ULTIMATE Mode (Multi-Process & Distributed Boost)
Designed for massive pipelines that spawn child processes (e.g., multi-GPU frameworks, distributed learning, parallel workers). It intercepts all child processes and binds them to specific cores.

```Python
from fasthardware import fasthardware
```

# Supercharge both main and all child processes recursively
```Python
fasthardware.speedup(mode="ULTIMATE")
```

# Your heavy multiprocessing/distributed pipeline here...
🧹 Manual Memory Sweeping (Optional)
For ultra-heavy asynchronous pipelines (e.g., blending AI inference with async API requests or audio generation), manually sweep the 0-generation memory cache without breaking your frame rate:

```Python
# Call this at the end of your loop iteration if necessary
fasthardware.manual_sweep()
```
📊 Performance Impact
Actual benchmarking on heavy real-time pipelines (YOLOv8 Inference + Parallel Workers):

Standard Python Implementation: ~30 FPS (with frequent micro-stutters and core thrashing)

With fasthardware (ULTIMATE Mode): 53+ FPS (Stable, zero core competition, 40%+ performance jump)

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

Developed with ⚡ by Choi Woongyo.
