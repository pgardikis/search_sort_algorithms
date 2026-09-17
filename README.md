# Search and Sort Algorithms

[![Tests](https://github.com/pgardikis/search-sort-algorithms/actions/workflows/tests.yml/badge.svg)](https://github.com/pgardikis/search-sort-algorithms/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.12%20%7C%203.14-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Merge Sort, Quick Sort, Linear Search, Binary Search and Interpolation Search, implemented from scratch in Python.

The program generates a list of random numbers, runs the algorithms on it and can time them against each other, so the difference between O(n) and O(log n) is something you can watch rather than just read about.

---

## Quick start

Requires Python 3.10 or newer. There are no dependencies.

```bash
git clone https://github.com/pgardikis/search-sort-algorithms.git
cd search-sort-algorithms
python3 -m search_sort
```

Or install it once to get a `search-sort` command that works from any folder:

```bash
pip install .
search-sort
```

---

## The algorithms

| Algorithm | Sorted input | Average | Worst | Extra space | Notes |
|:---|:---:|:---:|:---:|:---:|:---|
| **Merge Sort** | – | `O(n log n)` | `O(n log n)` | `O(n)` | Stable: equal numbers keep their order |
| **Quick Sort** | – | `O(n log n)` | `O(n²)` | `O(log n)` | Median-of-three pivot, three-way partition |
| **Linear Search** | no | `O(n)` | `O(n)` | `O(1)` | Checks every number in turn |
| **Binary Search** | yes | `O(log n)` | `O(log n)` | `O(1)` | Halves the range each step |
| **Interpolation Search** | yes | `O(log log n)` | `O(n)` | `O(1)` | Fastest when numbers are evenly spread |

> **Quick Sort's worst case is unlikely here.** The pivot is the median of three values and equal numbers are grouped in a single pass, so already sorted, reversed and repetitive lists all stay fast.

Sources: [`sorting.py`](search_sort/sorting.py) and [`searching.py`](search_sort/searching.py). Every function carries a docstring explaining how it works and what it costs.

---

## How it works

1. The program asks **how many random numbers** to generate: press Enter for 100,000, up to a maximum of 1,000,000. Each number is between 0 and 1,000,000.
2. It previews the list and **suggests a number that is in it**, so you have something to search for.
3. You pick an option:

```text
Choose an option
 1)Merge Sort
 2)Quick Sort
 3)Linear Search
 4)Binary Search
 5)Interpolation Search
 6)Generate a new random list
 7)Benchmark all algorithms
 0)EXIT
```

Binary and Interpolation Search sort the list with Merge Sort first, so the index they report is the position in the **sorted** list. Linear Search works on the list in its original order. The sorted copy is reused, so repeated searches do not sort again.

---

## Benchmark

Option **7** times every algorithm on random lists of 1,000, 10,000 and 100,000 numbers, keeping the fastest of three runs per measurement.

<details open>
<summary><b>Sorting a list</b> (milliseconds, lower is better)</summary>

| List size | Merge Sort | Quick Sort |
|---:|---:|---:|
| 1,000 | 1.055 | **0.720** |
| 10,000 | 13.120 | **9.087** |
| 100,000 | 144.514 | **112.164** |

</details>

<details open>
<summary><b>Finding one number</b> (microseconds, average of 200 searches)</summary>

| List size | Linear Search | Binary Search | Interpolation Search |
|---:|---:|---:|---:|
| 1,000 | 10.055 | 0.577 | **0.405** |
| 10,000 | 97.381 | 0.755 | **0.465** |
| 100,000 | 885.517 | 0.979 | **0.593** |

</details>

**What the numbers say:** a list 100 times longer makes Linear Search about 90 times slower, while Binary Search barely moves — `O(n)` against `O(log n)`, measured rather than assumed. Interpolation Search stays ahead of Binary Search because the random numbers are evenly spread, which is exactly the case it is built for. Quick Sort beats Merge Sort throughout, mostly because it swaps numbers in place instead of building new lists.

*Measured on one machine; your numbers will differ, but the shape of the curves will not.*

---

## Tests

```bash
pip install -e ".[test]"
pytest
```

91 tests covering:

- **Edge cases** — empty lists, single items, duplicates, negative numbers, already sorted and reversed input
- **Random lists** — hundreds of them per run, compared against Python's built-in `sorted()`
- **Regression tests** — the `IndexError` and divide-by-zero bugs this project started with
- **The menu and the benchmark** — input validation, the size limit, and the sorted list being reused

Every push runs them on Python 3.10, 3.12 and 3.14 through [GitHub Actions](.github/workflows/tests.yml).

---

## Project structure

```text
search_sort/
├── sorting.py      Merge Sort and Quick Sort
├── searching.py    Linear, Binary and Interpolation Search
├── cli.py          interactive menu and random list generation
├── benchmark.py    times the algorithms against each other
└── __main__.py     entry point for python3 -m search_sort
tests/              pytest suite for all of the above
pyproject.toml      package settings and pytest configuration
```

---

## License

[MIT](LICENSE)
