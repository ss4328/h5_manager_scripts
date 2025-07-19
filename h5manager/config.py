# h5manager/config.py
from __future__ import annotations
import os, pathlib, functools
import yaml

_DEFAULTS = {
    "image_dim": 300,
    "dtype": "int16",
    "output_dir": "~/datasets",
    "visualize": {"figsize": [12, 8]},
}

@functools.lru_cache(maxsize=1)
def _load_cfg() -> dict:
    """Return cascaded configuration (package defaults < user file < env var)."""
    cfg = _DEFAULTS.copy()
    # 1) project‑level default shipped with the wheel
    pkg_cfg = pathlib.Path(__file__).with_suffix(".yaml")
    if pkg_cfg.exists():
        cfg.update(yaml.safe_load(pkg_cfg.read_text()))
    # 2) user file ~/.h5manager/config.yaml
    user_cfg = pathlib.Path(os.getenv("H5MANAGER_CONFIG", "~/.h5manager/config.yaml")).expanduser()
    if user_cfg.exists():
        cfg.update(yaml.safe_load(user_cfg.read_text()))
    return cfg

def get(key: str, default=None):
    return _load_cfg().get(key, default)
