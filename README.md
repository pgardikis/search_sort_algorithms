# Algorithms for searching and sorting

[![Tests](https://github.com/pgardikis/search_sort_algorithms/actions/workflows/tests.yml/badge.svg)](https://github.com/pgardikis/search_sort_algorithms/actions/workflows/tests.yml)

Merge Sort, Quick Sort, Linear Search, Binary Search and Interpolation Search implemented from scratch in Python, without using Python's built-in sorting or searching.

## Algorithms

| Algorithm | File | List must be sorted | Time (average) | Time (worst) | Extra space |
|---|---|---|---|---|---|
| Merge Sort | `search_sort/sorting.py` | – | O(n log n) | O(n log n) | O(n) |
| Quick Sort | `search_sort/sorting.py` | – | O(n log n) | O(n^2)** | O(log n) |
| Linear Search | `search_sort/searching.py` | No | O(n) | O(n) | O(1) |
| Binary Search | `search_sort/searching.py` | Yes | O(log n) | O(log n) | O(1) |
| Interpolation Search | `search_sort/searching.py` | Yes | O(log log n)* | O(n) | O(1) |

\* when the numbers are evenly spread, which is the case for the random lists this program generates.

\*\* the pivot is the median of three values and equal numbers are grouped in one pass, so sorted, reversed and repeated-heavy lists stay fast in practice.

## Running

Requires Python 3.10 or newer. There are no other dependencies.

From the project folder:

```bash
python3 -m search_sort
```

Or install it once to get a `search-sort` command that works from any folder:

```bash
pip install .
search-sort
```

## How it works

1. The program asks how many random numbers to generate (press Enter for 100,000, up to 1,000,000). Each number is between 0 and 1,000,000.
2. It shows a preview of the list and suggests a number that is in it, so you have something to search for.
3. Pick an option from the menu:

```
 1)Merge Sort
 2)Quick Sort
 3)Linear Search
 4)Binary Search
 5)Interpolation Search
 6)Generate a new random list
 7)Benchmark all algorithms
 0)EXIT
```

Binary and Interpolation Search first sort the list with Merge Sort, so the index they report is the position in the sorted list. Linear Search works on the list in its original order.

## Benchmark

Menu option 7 times every algorithm on random lists of 1,000, 10,000 and 100,000 numbers. Results from one run:

**Sorting a list** (milliseconds, lower is better)

| List size | Merge Sort | Quick Sort |
|---:|---:|---:|
| 1,000 | 1.039 | **0.711** |
| 10,000 | 11.887 | **9.118** |
| 100,000 | 146.589 | **123.460** |

**Finding one number** (microseconds, average of 200 searches)

| List size | Linear Search | Binary Search | Interpolation Search |
|---:|---:|---:|---:|
| 1,000 | 9.397 | 0.599 | **0.427** |
| 10,000 | 116.133 | 0.873 | **0.532** |
| 100,000 | 932.197 | 1.401 | **0.698** |

Quick sort is consistently faster than merge sort here, and both grow in step with the list size. The searches show the difference between the complexities: a list 100 times longer makes linear search about 100 times slower, while binary search barely moves and interpolation search stays fastest because the random numbers are evenly spread.

## Running the tests

```bash
pip install -e ".[test]"
pytest
```

The tests compare the algorithms with Python's built-in `sorted()` on edge cases (empty lists, duplicates, negative numbers, missing numbers) and hundreds of random lists.

## Project structure

```
search_sort/
  sorting.py     Merge Sort and Quick Sort
  searching.py   Linear, Binary and Interpolation Search
  cli.py         interactive menu and random list generation
  benchmark.py   times the algorithms against each other
  __main__.py    lets you run the package with python3 -m search_sort
tests/           pytest tests for the algorithms, menu helpers and benchmark
pyproject.toml   package settings, makes it installable with pip
```

## License

[MIT](LICENSE)
