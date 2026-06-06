import os
import sys
import psutil
import gc

_current_process = psutil.Process(os.getpid())


def speedup(mode="DEFAULT"):
    print(f"\n [FASTHARDWARE V2] Tuning mode: {mode}...")

    _elevate_priority(_current_process)
    _optimize_runtime()
    _bind_c_libraries()

    if mode == "ULTIMATE":
        _supercharge_children()

    print(" [FASTHARDWARE V2] System hardware optimization complete.\n")


def _elevate_priority(process):
    try:
        if sys.platform == "win32":
            process.nice(psutil.HIGH_PRIORITY_CLASS)
        else:
            process.nice(-20)
    except Exception:
        pass


def _optimize_runtime():
    try:
        gc.disable()
        gc.set_threshold(700, 10, 10)
    except Exception:
        pass


def _bind_c_libraries():
    try:
        total_cores = str(os.cpu_count() or 4)
        for flag in ["OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"]:
            os.environ[flag] = total_cores
    except Exception:
        pass


def _supercharge_children():
    try:
        children = _current_process.children(recursive=True)
        if not children:
            print("   -> [MP] No child processes detected yet. Buffers ready.")
            return

        print(f"   -> [MP] Detecting {len(children)} child processes. Intercepting...")

        all_cores = list(range(os.cpu_count() or 4))
        if not all_cores:
            return

        for i, child in enumerate(children):
            try:
                if child.is_running():
                    _elevate_priority(child)
                    assigned_core = [all_cores[i % len(all_cores)]]
                    child.cpu_affinity(assigned_core)
                    print(f"      └─ Child [{child.pid}] Supercharged & Bound to Core {assigned_core}")
            except Exception:
                pass
    except Exception:
        pass


def manual_sweep():
    gc.enable()
    gc.collect(0)
    gc.disable()