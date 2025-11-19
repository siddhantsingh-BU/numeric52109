"""Statistics helpers for ``simple_package``.

Provides mean, median, standard deviation calculations with input
validation and a pretty-print function. The plotting functionality
lives in :mod:`simple_package.graphics`.

Notes on dependencies:
- These functions require ``numpy``. If ``numpy`` is not available an
  informative ``ImportError`` is raised when functions are called.
"""

from typing import Any, Dict

try:
	import numpy as np
except Exception:  # pragma: no cover - defensive import handling
	np = None


def _require_numpy():
	if np is None:
		raise ImportError(
			"This function requires the 'numpy' package. "
			"Install it with 'pip install numpy' and try again."
		)


def _as_array(data: Any) -> 'np.ndarray':
	_require_numpy()
	if isinstance(data, np.ndarray):
		return data
	if isinstance(data, (list, tuple)):
		return np.array(data)
	raise TypeError("Input data must be a list, tuple, or numpy.ndarray")


def mean(data: Any) -> float:
	"""Return the mean of `data`.

	Parameters
	- data: list/tuple or numpy array

	Raises
	- ImportError if numpy is not installed
	- TypeError if data is not a list/tuple/ndarray
	"""
	arr = _as_array(data)
	return float(np.mean(arr))


def median(data: Any) -> float:
	"""Return the median of `data`."""
	arr = _as_array(data)
	return float(np.median(arr))


def std(data: Any, ddof: int = 0) -> float:
	"""Return the standard deviation of `data`.

	Parameters
	- ddof: delta degrees of freedom (matches ``numpy.std``)
	"""
	arr = _as_array(data)
	return float(np.std(arr, ddof=ddof))


def summary(data: Any) -> Dict[str, float]:
	"""Return a dictionary with mean, median, std for `data`."""
	return {"mean": mean(data), "median": median(data), "std": std(data)}


def pretty_print(data: Any) -> None:
	"""Print a readable summary of the statistics for `data`.

	Example output:
		Count: 5
		Mean: 2.40
		Median: 2.00
		Std: 1.14
	"""
	_require_numpy()
	arr = _as_array(data)
	if arr.size == 0:
		print("No data to summarize (empty input).")
		return

	cnt = arr.size
	mu = mean(arr)
	med = median(arr)
	sd = std(arr)

	print(f"Count: {cnt}")
	print(f"Mean: {mu:.4g}")
	print(f"Median: {med:.4g}")
	print(f"Std: {sd:.4g}")

