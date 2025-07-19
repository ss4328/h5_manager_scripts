# h5manager/visualizer.py
from __future__ import annotations
import math, pathlib
import h5py, numpy as np, matplotlib.pyplot as plt
from matplotlib.backend_bases import KeyEvent


def _show_page(imgs: np.ndarray, idx0: int, n: int, axes):
    """Render n images starting at idx0 into a grid of Axes."""
    axes = np.ravel(axes)
    axes_n = len(axes)
    n_display = min(n, imgs.shape[0] - idx0)
    for ax in axes:
        ax.clear(); ax.axis("off")
    for i in range(n_display):
        j = idx0 + i
        img = imgs[j]
        if img.dtype != "uint8":
            img = img.astype("uint8")
        axes[i].imshow(img)
        axes[i].set_title(f"{j}", fontsize=8)
    for ax in axes[n_display:]:
        ax.set_visible(False)
    plt.tight_layout()


def visualize(file: pathlib.Path, per_page: int = 12) -> None:
    """
    Interactive viewer:
      ← / →  : previous / next page
      q      : quit
    """
    with h5py.File(file, "r") as hf:
        imgs = hf["images"]
        N = imgs.shape[0]
        per_page = max(1, per_page)
        ncols = 4
        nrows = math.ceil(per_page / ncols)
        page_size = nrows * ncols
        idx0 = 0  # first image index of current page

        fig, axes = plt.subplots(nrows, ncols, figsize=(12, 3 * nrows))
        _show_page(imgs, idx0, page_size, axes)
        fig.canvas.manager.set_window_title(f"{file.name}   ({N} images)")

        def on_key(event: KeyEvent):
            nonlocal idx0
            if event.key in ("right", "n"):
                idx0 = (idx0 + page_size) % N
            elif event.key in ("left", "p"):
                idx0 = (idx0 - page_size) % N
            elif event.key in ("q", "escape"):
                plt.close(fig); return
            else:
                return
            _show_page(imgs, idx0, page_size, axes)
            fig.canvas.draw_idle()

        fig.canvas.mpl_connect("key_press_event", on_key)
        plt.show()
