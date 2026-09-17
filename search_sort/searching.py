def linear_search(items, target):
    """Find a number by checking every item from the start.

    The list does not need to be sorted.

    Returns the index of the first item equal to target, or -1 if the
    number is not in the list.

    Time: O(n). Extra space: O(1).
    """
    for i, value in enumerate(items):  # checks the list items until it finds the required one
        if value == target:
            return i

    return -1

def binary_search(items, target):
    """Find a number in a sorted list by halving the search range.

    Compares target with the middle item and continues in the left or
    right half, until it finds the number or the range is empty.

    The list must be sorted in ascending order.

    Returns an index of target, or -1 if the number is not in the list.
    If the number appears more than once, any matching index may be returned.

    Time: O(log n). Extra space: O(1).
    """
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2  # calculates the middle index of the list
        if target < items[mid]:
            high = mid - 1  # checks at the left of the mid number
        elif target > items[mid]:
            low = mid + 1  # checks at the right of the mid number
        else:
            return mid  # the requested number is mid

    return -1

def interpolation_search(items, target):
    """Find a number in a sorted list by estimating where it should be.

    Instead of always checking the middle like binary search, it guesses
    the position from the number's value, the way you open a phone book
    near the right letter. This is fastest when values are evenly spread.

    The list must be sorted in ascending order.

    Returns an index of target, or -1 if the number is not in the list.
    If the number appears more than once, any matching index may be returned.

    Time: O(log log n) when values are evenly spread, O(n) in the worst case.
    Extra space: O(1).
    """
    low = 0
    high = len(items) - 1

    while low <= high and items[low] <= target <= items[high]:
        if items[high] == items[low]:  # all remaining numbers are equal, avoids division by zero
            return low if items[low] == target else -1

        pos = low + (high - low) * (target - items[low]) // (items[high] - items[low])

        if items[pos] == target:
            return pos
        elif target > items[pos]:
            low = pos + 1
        else:
            high = pos - 1

    return -1
