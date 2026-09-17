# Linear Search
def linear_search(items, target):
    for i, value in enumerate(items):  # checks the list items until it finds the required one
        if value == target:
            return i

    return -1

# Binary Search
def binary_search(items, target):
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

# Interpolation Search
def interpolation_search(items, target):
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
