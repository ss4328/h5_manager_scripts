# h5manager/converter.py
from __future__ import annotations
import pathlib, h5py, numpy as np
from PIL import Image
from . import config

def _preprocess(path: pathlib.Path, dim: int) -> np.ndarray:
    img = Image.open(path).convert("RGB")
    if img.size != (dim, dim):
        img = img.resize((dim, dim))
    return np.asarray(img, dtype=config.get("dtype", "int16"))

def convert_dir(input_dir: pathlib.Path, output_path: pathlib.Path, dim: int):
    """Convert all images in *input_dir* to a single HDF5 file *output_path*."""
    files = sorted(p for p in input_dir.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png"})
    if not files:
        raise ValueError(f"No images found in {input_dir}")
    data = np.stack([_preprocess(p, dim) for p in files])
    output_path = output_path.with_suffix(".h5")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with h5py.File(output_path, "w") as hf:
        hf.create_dataset("images", data=data, compression="gzip")
    return output_path
