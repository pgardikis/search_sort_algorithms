# Algorithms for searching and sorting

Merge Sort, Linear Search, Binary Search and Interpolation Search implemented from scratch in Python, without using Python's built-in sorting or searching.

## Algorithms

| Algorithm | File | List must be sorted | Time (average) | Time (worst) | Extra space |
|---|---|---|---|---|---|
| Merge Sort | `search_sort/sorting.py` | – | O(n log n) | O(n log n) | O(n) |
| Linear Search | `search_sort/searching.py` | No | O(n) | O(n) | O(1) |
| Binary Search | `search_sort/searching.py` | Yes | O(log n) | O(log n) | O(1) |
| Interpolation Search | `search_sort/searching.py` | Yes | O(log log n)* | O(n) | O(1) |

\* when the numbers are evenly spread, which is the case for the random lists this program generates.

## Running

Requires Python 3.9 or newer. There are no other dependencies.

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
 2)Linear Search
 3)Binary Search
 4)Interpolation Search
 5)Generate a new random list
 0)EXIT
```

Binary and Interpolation Search first sort the list with Merge Sort, so the index they report is the position in the sorted list. Linear Search works on the list in its original order.

## Running the tests

```bash
pip install -e ".[test]"
pytest
```

The tests compare the algorithms with Python's built-in `sorted()` on edge cases (empty lists, duplicates, negative numbers, missing numbers) and hundreds of random lists.

## Using the algorithms in your own code

```python
from search_sort.sorting import merge_sort
from search_sort.searching import binary_search

numbers = merge_sort([42, 7, 19, 7])  # [7, 7, 19, 42]
binary_search(numbers, 19)            # 2
binary_search(numbers, 100)           # -1 (not found)
```

## Project structure

```
search_sort/
  sorting.py     Merge Sort
  searching.py   Linear, Binary and Interpolation Search
  cli.py         interactive menu and random list generation
  __main__.py    lets you run the package with python3 -m search_sort
tests/           pytest tests for the algorithms and the menu helpers
pyproject.toml   package settings, makes it installable with pip
```
