import random

import pytest

from search_sort.searching import binary_search, interpolation_search, linear_search

SORTED_SEARCHES = [binary_search, interpolation_search]
ALL_SEARCHES = [linear_search, *SORTED_SEARCHES]

SORTED_CASES = [
    [],
    [7],
    [5, 5, 5, 5],
    [-7, -1, 0, 2, 3],
    [1, 2, 2, 2, 3, 9, 9],
    list(range(0, 1000, 10)),
]


@pytest.mark.parametrize("search", ALL_SEARCHES)
@pytest.mark.parametrize("numbers", SORTED_CASES)
def test_finds_every_number_in_the_list(search, numbers):
    for target in numbers:
        index = search(numbers, target)
        assert index != -1 and numbers[index] == target


@pytest.mark.parametrize("search", ALL_SEARCHES)
@pytest.mark.parametrize("numbers", SORTED_CASES)
def test_returns_minus_one_for_missing_numbers(search, numbers):
    for target in (-1000, 4, 5, 1000):
        if target not in numbers:
            assert search(numbers, target) == -1


def test_linear_search_returns_first_match_in_unsorted_list():
    assert linear_search([4, 9, 1, 9], 9) == 1


def test_binary_search_number_above_maximum():
    # used to raise IndexError
    assert binary_search([1, 2, 3], 99) == -1


def test_interpolation_search_all_equal_numbers():
    # used to raise ZeroDivisionError
    assert interpolation_search([5, 5, 5], 5) == 0
    assert interpolation_search([5, 5, 5], 6) == -1


@pytest.mark.parametrize("search", SORTED_SEARCHES)
def test_random_sorted_lists(search):
    rng = random.Random(42)
    for _ in range(300):
        numbers = sorted(rng.randint(-50, 50) for _ in range(rng.randint(0, 100)))
        target = rng.randint(-60, 60)
        index = search(numbers, target)
        if target in numbers:
            assert numbers[index] == target
        else:
            assert index == -1
