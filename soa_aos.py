import time
import numpy as np

# -------- settings --------
N = 5_000_000       # drop to 2_000_000 if memory is tight
REPEATS = 5
rng = np.random.default_rng(42)

# SoA: three separate contiguous arrays
x = rng.standard_normal(N)
y = rng.standard_normal(N)
z = rng.standard_normal(N)

def soa_numpy(x, y, z):
    # r2 = x^2 + y^2 + z^2
    return x*x + y*y + z*z

# AoS: structured dtype with interleaved fields
pts = np.empty(N, dtype=[('x','f8'), ('y','f8'), ('z','f8')])
pts['x'], pts['y'], pts['z'] = x, y, z

def aos_numpy(pts):
    return pts['x']*pts['x'] + pts['y']*pts['y'] + pts['z']*pts['z']

def bench(fn, *args, reps=REPEATS, label=""):
    # warm-up
    out = fn(*args)
    _ = float(out[:10].sum())   # touch output
    best = float('inf')
    for _ in range(reps):
        t0 = time.perf_counter()
        out = fn(*args)
        dt = time.perf_counter() - t0
        if dt < best:
            best = dt
    print(f"{label:14s} best = {best:.4f}s")
    return best

print(f"N={N:,}")
t_soa = bench(soa_numpy, x, y, z, label="SoA NumPy")
t_aos = bench(aos_numpy, pts,      label="AoS NumPy")
print(f"\nSpeedup (SoA over AoS): {t_aos/t_soa:.2f}x")

import csv
with open("aos_soa_results.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["variant", "best_seconds"])
    w.writerow(["SoA_NumPy", t_soa])
    w.writerow(["AoS_NumPy", t_aos])
print("Wrote aos_soa_results.csv")

