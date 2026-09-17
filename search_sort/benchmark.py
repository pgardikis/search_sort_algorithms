"""Time the algorithms against each other on random lists."""

import random
from time import perf_counter
from typing import NamedTuple

from .searching import binary_search, interpolation_search, linear_search
from .sorting import merge_sort, quick_sort

SIZES = (1000, 10000, 100000)
SEARCHES_PER_SIZE = 200
REPEATS = 3  # each measurement is taken a few times and the fastest one is kept

SORTS = [("Merge Sort", merge_sort), ("Quick Sort", quick_sort)]
SEARCHES = [
    ("Linear Search", linear_search, False),
    ("Binary Search", binary_search, True),
    ("Interpolation Search", interpolation_search, True),
]


class Result(NamedTuple):
    """Timings for one list size."""

    size: int
    sorts: dict  # algorithm name -> seconds to sort the list
    searches: dict  # algorithm name -> average seconds to find one number
    searches_per_size: int


def fastest(repeat, function, *args):
    """Run something a few times and return the shortest time it took, in seconds."""
    best = None
    for _ in range(repeat):
        start = perf_counter()
        function(*args)
        taken = perf_counter() - start
        if best is None or taken < best:
            best = taken
    return best


def random_numbers(size, max_value, rng):
    """Return `size` random numbers between 0 and `max_value`."""
    return [rng.randint(0, max_value) for _ in range(size)]


def time_sorts(numbers, repeat=REPEATS):
    """Return the seconds each sort takes on one list."""
    return {name: fastest(repeat, sort, numbers) for name, sort in SORTS}


def time_searches(numbers, targets, repeat=REPEATS):
    """Return the average seconds each search takes to find one number."""
    ordered = merge_sort(numbers)
    results = {}
    for name, search, needs_sorted in SEARCHES:
        items = ordered if needs_sorted else numbers
        taken = fastest(repeat, search_all, search, items, targets)
        results[name] = taken / len(targets)
    return results


def search_all(search, items, targets):
    for target in targets:
        search(items, target)


def run(
    sizes=SIZES,
    searches_per_size=SEARCHES_PER_SIZE,
    max_value=None,
    seed=None,
    repeat=REPEATS,
):
    """Time every algorithm on a random list of each size.

    The numbers of each list run from 0 to `max_value`, or to ten times the
    list size when `max_value` is left out, which keeps them evenly spread.
    Pass a `seed` to generate the same lists every time.

    Returns one Result per size.
    """
    rng = random.Random(seed)
    results = []
    for size in sizes:
        top = max_value if max_value is not None else size * 10
        numbers = random_numbers(size, top, rng)
        targets = [rng.choice(numbers) for _ in range(searches_per_size)]
        results.append(
            Result(
                size=size,
                sorts=time_sorts(numbers, repeat),
                searches=time_searches(numbers, targets, repeat),
                searches_per_size=searches_per_size,
            )
        )
    return results


def format_table(results):
    """Turn results into a table: sorts in milliseconds, searches in microseconds."""
    lines = ["Sorting a list (milliseconds)"]
    names = [name for name, _ in SORTS]
    lines.append(_header(names))
    for result in results:
        lines.append(_row(result.size, [result.sorts[name] * 1000 for name in names]))

    searches_per_size = results[0].searches_per_size if results else SEARCHES_PER_SIZE
    names = [name for name, _, _ in SEARCHES]
    lines.append("")
    lines.append(f"Finding one number (microseconds, average of {searches_per_size} searches)")
    lines.append(_header(names))
    for result in results:
        lines.append(_row(result.size, [result.searches[name] * 1000000 for name in names]))
    return "\n".join(lines)


def _header(names):
    return f"{'size':>10}  " + "  ".join(f"{name:>20}" for name in names)


def _row(size, values):
    return f"{size:>10}  " + "  ".join(f"{value:>20.3f}" for value in values)
