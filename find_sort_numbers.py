def main():
    file_t = raw_input("Enter txt filename or path: ")
    find_sort(file_t)

def find_sort(filename):
    lst = file_toList(filename)

    while(1):
        print(" \nChoose an option\n 1)Merge Sort\n 2)Linear Search\n 3)Binary Search\n 4)Interpolation Search\n 0)EXIT\n")
        choice = str(input("Enter your option's number: "))

        if choice == "1":
            print("The sorted list is", merge_sort(lst))
        elif choice == "2":
            number = int(input("Enter the number you want to find it's index: "))
            print("Starting Linear Search for number", number, "in list", lst)
            index = linear_search(lst, number)
            if index != -1:
                print("Number found at index ", index)
            else:
                print("Number not found!")
        elif choice == "3":
            number = int(input("Enter the number you want to find it's index: "))
            lst.sort()
            print("Starting Binary Search for number", number, "in list", lst)
            index = binary_search(lst, 0, len(lst), number)
            if index != -1:
                print("Number found at index ", index)
            else:
                print("Number not found!")
        elif choice == "4":
            number = int(input("Enter the number you want to find it's index: "))
            lst.sort()
            print("Starting Interpolation Search for number", number, "in list", lst)
            index = interpolation_search(lst, number)
            if index != -1:
                print("Number found at index ", index)
            else:
                print("Number not found!")
        elif choice == "0":
            exit()
        else:
            print("Try again, choice", choice,"doesn't exist!")

def file_toList(ftl):
    with open(ftl) as f:
        ilist = f.read().splitlines()
        ilist = [int(i) for i in ilist]

    return ilist

# Merge Sort
def merge_sort(mlst):

    print("Splitting", mlst)
    if len(mlst) > 1:
        mid = len(mlst) // 2 # finds the median number of the list and separates the list into two new lists
        lhalf = mlst[:mid]
        rhalf = mlst[mid:]

        merge_sort(lhalf)
        merge_sort(rhalf)

        i = 0
        j = 0
        k = 0

        while len(lhalf) > i and len(rhalf) > j:
            if lhalf[i] < rhalf[j]:
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
        print("Merging", mlst)
    return mlst

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

    mid = (low + high) // 2  # calculates the middle nummber of the list
    if num_to_find < blst[mid]:
        return binary_search(blst, low, mid - 1, num_to_find) # checks at the right of the mid number
    elif num_to_find > blst[mid]:
        return binary_search(blst, mid + 1, high, num_to_find) # checks at the left of the mid number
    else:
        return mid # the requested number is mid

def interpolation_search(ilst, num_to_find):
    high = len(ilst) - 1
    low = 0

    while (low<=high) and (num_to_find >= ilst[low]) and (num_to_find <= ilst[high]):
        pos = int( low + (float((high - low)/(ilst[high] - ilst[low])) * (num_to_find - ilst[low])))

        if ilst[pos] == num_to_find:
            return pos
        elif num_to_find > ilst[pos]:
            low = pos + 1
        else:
            high = pos -1

    return -1

if __name__ == "__main__":
    main()
