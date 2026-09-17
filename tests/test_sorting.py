import random

import pytest

from search_sort import sorting
from search_sort.sorting import merge_sort, quick_sort

EDGE_CASES = [
    [],
    [7],
    [2, 1],
    [5, 5, 5, 5],
    [3, -1, 0, -7, 2],
    list(range(50)),
    list(range(50, 0, -1)),
]


SORTS = [merge_sort, quick_sort]


@pytest.mark.parametrize("sort", SORTS)
@pytest.mark.parametrize("numbers", EDGE_CASES)
def test_sorts_edge_cases(sort, numbers):
    assert sort(numbers) == sorted(numbers)


@pytest.mark.parametrize("sort", SORTS)
def test_sorts_random_lists(sort):
    rng = random.Random(42)
    for _ in range(300):
        numbers = [rng.randint(-100, 100) for _ in range(rng.randint(0, 200))]
        assert sort(numbers) == sorted(numbers)


@pytest.mark.parametrize("sort", SORTS)
def test_does_not_change_the_input(sort):
    numbers = [3, 1, 2]
    sort(numbers)
    assert numbers == [3, 1, 2]


@pytest.mark.parametrize("sort", SORTS)
def test_returns_a_new_list(sort):
    numbers = [1]
    assert sort(numbers) is not numbers


@pytest.mark.parametrize("sort", SORTS)
@pytest.mark.parametrize(
    "numbers",
    [list(range(2000)), list(range(2000, 0, -1)), [7] * 2000],
    ids=["already-sorted", "reversed", "all-equal"],
)
def test_sorts_arranged_input_correctly(sort, numbers):
    assert sort(numbers) == sorted(numbers)


@pytest.mark.parametrize(
    "arrange",
    [
        lambda n: list(range(n)),
        lambda n: list(range(n, 0, -1)),
        lambda n: list(range(n // 2)) + list(range(n // 2, 0, -1)),
    ],
    ids=["already-sorted", "reversed", "organ-pipe"],
)
def test_quick_sort_splits_arranged_input_evenly(arrange, monkeypatch):
    """Quick sort must not degrade to O(n^2) on tidy input.

    It once picked its pivot from the first, middle and last numbers,
    which made sorted, reversed and organ-pipe lists take quadratic time:
    2.8x slower per doubling, and 25 seconds for 150,000 numbers.

    Counting the numbers each partition walks over measures that directly,
    without depending on how fast the machine is. Good splits scan about
    n * log2(n) numbers in total; the old pivot scanned 17x more.
    """
    size = 20000
    budget = size * 40  # n * log2(n) is about 14 * n here, so this leaves room to spare

    scanned = 0
    real_partition = sorting._partition

    def counting_partition(items, low, high):
        nonlocal scanned
        scanned += high - low + 1
        return real_partition(items, low, high)

    monkeypatch.setattr(sorting, "_partition", counting_partition)
    assert sorting.quick_sort(arrange(size)) == sorted(arrange(size))
    assert scanned < budget, f"scanned {scanned:,} numbers, expected under {budget:,}"
