"""GPU-hour ledger. Wrap every job so compute per round can be reported (PS: GPU-hours incl. failed runs).

    with gpu_job("round1/sft_qwen3tts", n_gpus=4, gpu_type="L4"):
        train()
"""
from __future__ import annotations

import csv
import os
import socket
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

LEDGER = Path(os.environ.get("RIMET2_LEDGER", "runs/compute_ledger.csv"))
COLS = ["start_utc", "job", "round", "n_gpus", "gpu_type", "wall_h", "gpu_h", "status", "host", "notes"]


def _visible_gpus() -> int:
    v = os.environ.get("CUDA_VISIBLE_DEVICES")
    if v is not None and v.strip() != "":
        return len([x for x in v.split(",") if x.strip() != ""])
    try:
        import torch

        return torch.cuda.device_count()
    except Exception:
        return 0


@contextmanager
def gpu_job(job: str, n_gpus: int | None = None, gpu_type: str = "L4", round_: int | str = "", notes: str = "",
            ledger: Path | None = None):
    ledger = Path(ledger or LEDGER)
    ledger.parent.mkdir(parents=True, exist_ok=True)
    n = _visible_gpus() if n_gpus is None else n_gpus
    t0 = time.time()
    start = datetime.now(timezone.utc).isoformat(timespec="seconds")
    status = "ok"
    try:
        yield
    except BaseException:
        status = "failed"
        raise
    finally:
        wall_h = (time.time() - t0) / 3600.0
        new = not ledger.exists()
        with open(ledger, "a", newline="") as f:
            w = csv.writer(f)
            if new:
                w.writerow(COLS)
            w.writerow([start, job, round_, n, gpu_type, f"{wall_h:.4f}", f"{wall_h * n:.4f}", status,
                        socket.gethostname(), notes])


def total_gpu_hours(ledger: Path | None = None, round_: str | None = None) -> float:
    ledger = Path(ledger or LEDGER)
    if not ledger.exists():
        return 0.0
    with open(ledger) as f:
        rows = list(csv.DictReader(f))
    return sum(float(r["gpu_h"]) for r in rows if round_ is None or str(r["round"]) == str(round_))
