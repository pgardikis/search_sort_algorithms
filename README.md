# Search and Sort Algorithms

[![Tests](https://github.com/pgardikis/search-sort-algorithms/actions/workflows/tests.yml/badge.svg)](https://github.com/pgardikis/search-sort-algorithms/actions/workflows/tests.yml)
[![Lint](https://github.com/pgardikis/search-sort-algorithms/actions/workflows/lint.yml/badge.svg)](https://github.com/pgardikis/search-sort-algorithms/actions/workflows/lint.yml)
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
| **Quick Sort** | – | `O(n log n)` | `O(n²)` | `O(log n)` | Random pivot, three-way partition |
| **Linear Search** | no | `O(n)` | `O(n)` | `O(1)` | Checks every number in turn |
| **Binary Search** | yes | `O(log n)` | `O(log n)` | `O(1)` | Halves the range each step |
| **Interpolation Search** | yes | `O(log log n)` | `O(n)` | `O(1)` | Fastest when numbers are evenly spread |

> **Quick Sort's worst case does not depend on the input.** The pivot is picked at random, so no arrangement of the numbers is reliably slow, and equal numbers are grouped in a single pass, which makes repetitive lists very fast. Picking the pivot from fixed positions instead is what [used to make tidy input quadratic](search_sort/sorting.py).

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
| 1,000 | 0.898 | **0.784** |
| 10,000 | 11.470 | **10.517** |
| 100,000 | 136.416 | **133.550** |

</details>

<details open>
<summary><b>Finding one number</b> (microseconds, average of 200 searches)</summary>

| List size | Linear Search | Binary Search | Interpolation Search |
|---:|---:|---:|---:|
| 1,000 | 8.907 | 0.537 | **0.413** |
| 10,000 | 94.229 | 0.749 | **0.502** |
| 100,000 | 857.402 | 0.973 | **0.605** |

</details>

**What the numbers say:** a list 100 times longer makes Linear Search about 90 times slower, while Binary Search barely moves — `O(n)` against `O(log n)`, measured rather than assumed. Interpolation Search stays ahead of Binary Search because the random numbers are evenly spread, which is exactly the case it is built for. The two sorts are close on random input, and which one wins depends on how the numbers are arranged:

<details>
<summary><b>The same sorts on arranged input</b> (milliseconds, 100,000 numbers)</summary>

| Arrangement | Merge Sort | Quick Sort |
|:---|---:|---:|
| Random | 141 | **138** |
| Already sorted | **85** | 126 |
| Reversed | **88** | 121 |
| Organ pipe (up then down) | **89** | 109 |
| All numbers equal | 83 | **3** |

Merge Sort is quicker on tidy input, because a merge of two already ordered halves ends early. Quick Sort wins by a wide margin when the list is full of repeats, because its three-way partition puts every equal number in place in a single pass.

</details>

*Measured on one machine; your numbers will differ, but the shape of the curves will not.*

---

## Tests

```bash
pip install -e ".[test]"
pytest
```

The suite covers:

- **Edge cases** — empty lists, single items, duplicates, negative numbers, already sorted and reversed input
- **Random lists** — hundreds of them per run, compared against Python's built-in `sorted()`
- **Regression tests** — the `IndexError`, divide-by-zero and quadratic-pivot bugs this project has had
- **The menu and the benchmark** — input validation, the size limit, and the sorted list being reused

Every push runs them on Python 3.10, 3.12 and 3.14 through [GitHub Actions](.github/workflows/tests.yml), and a second workflow checks the code with [ruff](.github/workflows/lint.yml).

---

## Project structure

```text
search_sort/
├── __init__.py     marks the folder as a package
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
