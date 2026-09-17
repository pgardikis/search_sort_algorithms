"""Time the algorithms against each other on random lists."""

import random
from time import perf_counter

from .searching import binary_search, interpolation_search, linear_search
from .sorting import merge_sort, quick_sort

SIZES = (1000, 10000, 100000)
SEARCHES_PER_SIZE = 200

SORTS = [("Merge Sort", merge_sort), ("Quick Sort", quick_sort)]
SEARCHES = [
    ("Linear Search", linear_search, False),
    ("Binary Search", binary_search, True),
    ("Interpolation Search", interpolation_search, True),
]


def time_sorts(numbers):
    """Return the seconds each sort takes on one list."""
    results = {}
    for name, sort in SORTS:
        start = perf_counter()
        sort(numbers)
        results[name] = perf_counter() - start
    return results


def time_searches(numbers, targets):
    """Return the average seconds each search takes for one number."""
    sorted_numbers = merge_sort(numbers)
    results = {}
    for name, search, needs_sorted in SEARCHES:
        items = sorted_numbers if needs_sorted else numbers
        start = perf_counter()
        for target in targets:
            search(items, target)
        results[name] = (perf_counter() - start) / len(targets)
    return results


def run(sizes=SIZES, searches_per_size=SEARCHES_PER_SIZE, max_value=None, seed=None):
    """Time every algorithm on a random list of each size.

    Returns one row per size: (size, sort seconds, average search seconds).
    """
    rng = random.Random(seed)
    rows = []
    for size in sizes:
        top = max_value if max_value is not None else size * 10
        numbers = [rng.randint(0, top) for _ in range(size)]
        targets = [rng.choice(numbers) for _ in range(searches_per_size)]
        rows.append((size, time_sorts(numbers), time_searches(numbers, targets)))
    return rows


def format_table(rows):
    """Turn benchmark rows into a table, sorts in milliseconds and searches in microseconds."""
    lines = []
    names = [name for name, _ in SORTS]
    lines.append("Sorting a list (milliseconds)")
    lines.append(header(names))
    for size, sorts, _ in rows:
        lines.append(row(size, [sorts[name] * 1000 for name in names]))

    names = [name for name, _, _ in SEARCHES]
    lines.append("")
    lines.append("Finding one number (microseconds, average of {} searches)".format(SEARCHES_PER_SIZE))
    lines.append(header(names))
    for size, _, searches in rows:
        lines.append(row(size, [searches[name] * 1000000 for name in names]))
    return "\n".join(lines)


def header(names):
    return "{:>10}  ".format("size") + "  ".join("{:>20}".format(name) for name in names)


def row(size, values):
    return "{:>10}  ".format(size) + "  ".join("{:>20.3f}".format(value) for value in values)
