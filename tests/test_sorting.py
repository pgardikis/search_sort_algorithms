import random

import pytest

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
def test_returns_a_new_list(sort, numbers=None):
    numbers = [1]
    assert sort(numbers) is not numbers


@pytest.mark.parametrize("sort", SORTS)
@pytest.mark.parametrize(
    "numbers",
    [list(range(2000)), list(range(2000, 0, -1)), [7] * 2000],
    ids=["already-sorted", "reversed", "all-equal"],
)
def test_handles_worst_case_inputs_quickly(sort, numbers):
    # these inputs make a naive quick sort slow or hit the recursion limit
    assert sort(numbers) == sorted(numbers)


def test_is_stable():
    # equal keys must keep their original order
    class Item:
        def __init__(self, key, label):
            self.key, self.label = key, label

        def __le__(self, other):
            return self.key <= other.key

    items = [Item(1, "a"), Item(0, "b"), Item(1, "c"), Item(0, "d")]
    assert [item.label for item in merge_sort(items)] == ["b", "d", "a", "c"]
