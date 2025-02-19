# make-slice

Creates slice objects with clean syntax.

[![PyPI](https://img.shields.io/pypi/v/make-slice?logo=pypi&label=PyPI%20package)](https://pypi.org/project/make-slice/)
[![cov](https://0x00-pl.github.io/make_slice/badges/coverage.svg)](https://github.com/0x00-pl/make_slice/actions)

## Install

```bash
pip install make-slice
```

## Usage

```python
from make_slice import make_slice

my_list = list(range(5))  # list: [0, 1, 2, 3, 4]
# Create a slice object
rev_slice = make_slice[::-1]  # Equivalent to slice(None, None, -1)
# Use the slice object
print(my_list[rev_slice])  # Output: [4, 3, 2, 1, 0]
```


## License

MIT License - See [LICENSE](LICENSE) for details.
