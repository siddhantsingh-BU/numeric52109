"""Plotting helpers for ``simple_package``.

Contains a convenience function to plot a histogram with mean and median
marked. Requires ``numpy`` and ``matplotlib``. If either is missing an
informative ``ImportError`` is raised.
"""
from typing import Any, Optional

try:
    import numpy as np
except Exception:  # pragma: no cover - handled at call time
    np = None

try:
    import matplotlib.pyplot as plt
except Exception:  # pragma: no cover
    plt = None


def _require_deps():
    if np is None:
        raise ImportError(
            "The plotting functions require 'numpy'. Install it with 'pip install numpy'."
        )
    if plt is None:
        raise ImportError(
            "The plotting functions require 'matplotlib'. Install it with 'pip install matplotlib'."
        )


def plot_histogram(data: Any, bins: int = 10, title: Optional[str] = None,
                   show: bool = True, savepath: Optional[str] = None) -> None:
    """Plot a histogram of `data` with mean and median marked.

    Parameters
    - data: list/tuple or numpy array
    - bins: number of histogram bins
    - title: optional plot title
    - show: whether to call ``plt.show()``
    - savepath: if provided, save the figure to this path
    """
    _require_deps()
    if isinstance(data, (list, tuple)):
        arr = np.array(data)
    elif isinstance(data, np.ndarray):
        arr = data
    else:
        raise TypeError("Input data must be a list, tuple, or numpy.ndarray")

    if arr.size == 0:
        raise ValueError("Cannot plot an empty dataset")

    mu = float(np.mean(arr))
    med = float(np.median(arr))

    fig, ax = plt.subplots()
    ax.hist(arr, bins=bins, alpha=0.7, color='C0')
    ax.axvline(mu, color='C1', linestyle='--', linewidth=2, label=f'Mean ({mu:.3g})')
    ax.axvline(med, color='C2', linestyle=':', linewidth=2, label=f'Median ({med:.3g})')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.legend()
    if title:
        ax.set_title(title)
    else:
        ax.set_title('Histogram')

    if savepath:
        fig.savefig(savepath, bbox_inches='tight')

    if show:
        plt.show()
    plt.close(fig)
