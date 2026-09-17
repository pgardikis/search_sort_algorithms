"""Sorting algorithms.

Both sorts return a new sorted list and leave the list you pass in
unchanged. Merge sort is stable, quick sort is not.
"""

from random import randrange


def merge_sort(items):
    """Sort a list of numbers using merge sort.

    Splits the list into two halves, sorts each half, then merges the
    two sorted halves into one. Equal numbers keep their original order.

    Returns a new sorted list. The input list is not changed.

    Time: O(n log n). Extra space: O(n).
    """
    if len(items) <= 1:
        return list(items)

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= keeps equal numbers in their original order
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # one half is used up, the rest of the other half is already sorted
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(items):
    """Sort a list of numbers using quick sort.

    Picks a pivot, moves smaller numbers before it and larger numbers
    after it, then sorts those two parts the same way. Numbers equal to
    the pivot land in the middle and need no further sorting, so lists
    with many repeated numbers stay fast.

    The pivot is picked at random, so no particular arrangement of the
    input is slow: sorted, reversed and repetitive lists all behave like
    random ones. A run can still be unlucky, but not because of the data.

    Not stable: equal numbers may end up in a different order than they
    started. Returns a new sorted list. The input list is not changed.

    Time: O(n log n) expected, O(n^2) in the worst case.
    Extra space: O(log n) for the recursion.
    """
    result = list(items)
    _quick_sort(result, 0, len(result) - 1)
    return result


def _quick_sort(items, low, high):
    while low < high:
        lt, gt = _partition(items, low, high)

        # recurse into the smaller side and loop on the larger one, which
        # keeps the recursion shallow even on already sorted lists
        if lt - low < high - gt:
            _quick_sort(items, low, lt - 1)
            low = gt + 1
        else:
            _quick_sort(items, gt + 1, high)
            high = lt - 1


def _partition(items, low, high):
    """Move numbers smaller than the pivot to the left and larger ones to the right.

    Returns the first and last index of the numbers equal to the pivot,
    which are already in their final place.

    A random pivot is what keeps the split even. Sampling fixed positions
    such as the first, middle and last number looks reasonable but pairs
    badly with the partition below, which leaves the larger-than side
    rotated, so on sorted input those samples keep picking near-smallest
    pivots and the sort slows to a crawl.
    """
    pivot = items[randrange(low, high + 1)]
    lt = low
    gt = high
    i = low

    while i <= gt:
        if items[i] < pivot:
            items[lt], items[i] = items[i], items[lt]
            lt += 1
            i += 1
        elif items[i] > pivot:
            items[i], items[gt] = items[gt], items[i]
            gt -= 1
        else:
            i += 1

    return lt, gt
