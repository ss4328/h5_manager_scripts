# h5manager/merger.py
from __future__ import annotations
import h5py, pathlib, glob, numpy as np

def _expand(patterns: str) -> list[pathlib.Path]:
    pats = [p.strip() for p in patterns.split(",")]
    return [pathlib.Path(p) for pat in pats for p in glob.glob(pat)]

def merge(inputs: str, output: pathlib.Path):
    """Concatenate the *images* dataset from multiple .h5 files."""
    files = _expand(inputs)
    if not files:
        raise FileNotFoundError(f"No matching files for pattern(s): {inputs}")
    data = []
    for f in files:
        with h5py.File(f, "r") as hf:
            data.append(hf["images"][...])
    merged = np.concatenate(data, axis=0)
    output = output.with_suffix(".h5")
    with h5py.File(output, "w") as hf:
        hf.create_dataset("images", data=merged, compression="gzip")
    return output
