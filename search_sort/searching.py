# Linear Search
def linear_search(llst, num_to_find):

    for i in range(len(llst)):  # checks the list items until it finds the required one
        if num_to_find == llst[i]:
            return i

    return -1

# Binary Search
def binary_search(blst, low, high, num_to_find):

    if high < low:
        return -1

    mid = (low + high) // 2  # calculates the middle index of the list
    if num_to_find < blst[mid]:
        return binary_search(blst, low, mid - 1, num_to_find) # checks at the left of the mid number
    elif num_to_find > blst[mid]:
        return binary_search(blst, mid + 1, high, num_to_find) # checks at the right of the mid number
    else:
        return mid # the requested number is mid

# Interpolation Search
def interpolation_search(ilst, num_to_find):
    high = len(ilst) - 1
    low = 0

    while (low <= high) and (num_to_find >= ilst[low]) and (num_to_find <= ilst[high]):
        if ilst[high] == ilst[low]:  # all remaining numbers are equal, avoids division by zero
            return low if ilst[low] == num_to_find else -1

        pos = low + (high - low) * (num_to_find - ilst[low]) // (ilst[high] - ilst[low])

        if ilst[pos] == num_to_find:
            return pos
        elif num_to_find > ilst[pos]:
            low = pos + 1
        else:
            high = pos - 1

    return -1
