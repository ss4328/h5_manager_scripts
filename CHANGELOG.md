# Changelog

All notable changes to h5manager will be documented in this file.
This project adheres to [Semantic Versioning](https://semver.org/).

## [0.1.0] – 2025‑07‑19

### Added

* First public release on TestPyPI / PyPI.
* Typer‑based CLI (h5manager convert | merge | visualize).
* Image‑to‑HDF5 converter with configurable resize dimension & dtype.
* HDF5 merger with shape validation & optional shuffle.
* Interactive visualizer (arrow‑key paging, up to 12 imgs per page).
* config.py with YAML‑overridable defaults.
* Example images & quick‑start commands in README.md.
* Packaging via Hatchling (pyproject.toml).

### Changed

* Legacy scripts (h5Converter.py, mergeh5.py, …) refactored into importable modules under h5manager/.
* Replaced Python‑2 style prints with f‑strings; removed hard‑coded paths.

### Fixed
* Consistent dataset name images across all modules.
* Visualizer colour cast when storing int16 pixel data.

### Removed
* Deprecated shell wrapper datasets2h5.sh.
* Large sample image folders from source distribution (kept in repo; wheel ships without them).
* Legacy scripts