"""Package initializer for `simple_package`.

Expose the main calculator operations at package level so that
`import simple_package as sp` allows using `sp.add`, `sp.subtract`, etc.
"""

from .operations import (
	add,
	subtract,
	multiply,
	divide,
	calculator_interface,
)
from .statistics import (
	mean,
	median,
	std,
	summary,
	pretty_print,
)
from .graphics import (
	plot_histogram,
)

__all__ = [
	'add',
	'subtract',
	'multiply',
	'divide',
	'calculator_interface',
	'mean',
	'median',
	'std',
	'summary',
	'pretty_print',
	'plot_histogram',
]