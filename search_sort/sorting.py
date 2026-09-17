# Merge Sort
def merge_sort(items):
    if len(items) <= 1:
        return list(items)

    mid = len(items) // 2  # finds the middle index of the list and separates the list into two halves
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
