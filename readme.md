# H5 Manager
H5 Manager is a tiny, battery‑included toolkit that turns folders of images into tidy HDF5 datasets, stitches those datasets together, and lets you flip through them in seconds — all from a single command‑line interface.

## Background

While experimenting with computer‑vision side projects I kept bouncing between raw JPEG folders and different HDF5 ad‑hoc scripts. Each time I forgot a flag or lost the code snippet. H5 Manager is my attempt to freeze that knowledge into a reusable, well‑tested package:

* Convert an arbitrary image tree into a single images dataset (uint8 | int16) with one flag.
* Merge any number of compatible .h5 files (optionally shuffled).
* Visualise the first few or page through the whole set with arrow keys.
* Configure defaults in ~/.h5manager/config.yaml or an env var.
* Ships tiny example data & pytest suite so CI and newcomers can try it instantly.

If you’ve ever asked yourself…

“What even is an HDF5 file and why should I care?”
“Why does storing 10 k images in folders grind my dataloader?”
“Which one‑liner will regenerate this dataset six months from now?”

…then this repo is for you.


## Installation

```bash
git@github.com:ss4328/h5_manager_scripts.git
pip install -e 
```

## CLI Quickstart 

```bash
# 1 Convert two image folders (resize to 64×64)
h5manager convert example_img_dir/seefood/test/hot_dog      \
               --output tmp/hotdog_64 --dim 64

h5manager convert example_img_dir/seefood/test/not_hot_dog  \
               --output tmp/nothotdog_64 --dim 64

# 2 Merge them into one dataset
h5manager merge --inputs tmp/hotdog_64.h5,tmp/nothotdog_64.h5 \
                --output tmp/merged

# 3 Browse interactively (p/n to page)
h5manager visualize tmp/merged.h5
```

Screenshots below show the pager in action — notice the mix of classes once you hit →.
<img width="1214" height="971" alt="hotfdog_64" src="https://github.com/user-attachments/assets/fb085f35-9f1f-4686-a9b5-0cd9853dfb14" />
<img width="1198" height="961" alt="nothotdog_64" src="https://github.com/user-attachments/assets/c4589d97-8720-4a82-a382-c4f3eb4ee7af" />
<img width="1207" height="964" alt="merged" src="https://github.com/user-attachments/assets/1a49db4c-8275-4078-ad10-b5509e92c9e3" />

## FAQ

Why not keep raw folders?
* HDF5 offers compression, contiguous storage, random access, and zero filesystem overhead per image. Large CV datasets load 3‑10 × faster.

Does this replace TFRecord / LMDB?
* No – it’s a lightweight alternative when you prefer pure‑Python tooling and the HDF5 ecosystem.

Can I store labels?
* For now the CLI is image‑only; add extra datasets (labels, bboxes) via h5py or open an issue for a feature request.

## Contributing & roadmap

1. Shrink example dataset in examples/images/ (< 1 MB).
2. Add Streamlit GUI (h5manager gui).
3. Lazy / chunked writer for huge datasets.
Pull requests & bug reports are very welcome!

## Acknowledgements

- National Center for Supercomputing Applications — creators of HDF5.
- Tomacz Golan — original mergeh5.py inspiration.
- [NEON Science blog](https://www.neonscience.org/resources/learning-hub/tutorials/about-hdf5) — approachable HDF5 primer.

Released under the MIT License.   © 2025 Shivansh Suhane

  
