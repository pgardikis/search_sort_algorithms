# Merge Sort
def merge_sort(mlst):

    if len(mlst) > 1:
        mid = len(mlst) // 2 # finds the middle index of the list and separates the list into two new lists
        lhalf = mlst[:mid]
        rhalf = mlst[mid:]

        merge_sort(lhalf)
        merge_sort(rhalf)

        i = 0
        j = 0
        k = 0

        while len(lhalf) > i and len(rhalf) > j:
            if lhalf[i] <= rhalf[j]:
                mlst[k] = lhalf[i]
                i += 1
            else:
                mlst[k] = rhalf[j]
                j += 1
            k += 1
        while len(lhalf) > i:
            mlst[k] = lhalf[i]
            i += 1
            k += 1
        while len(rhalf) > j:
            mlst[k] = rhalf[j]
            j += 1
            k += 1
    return mlst
