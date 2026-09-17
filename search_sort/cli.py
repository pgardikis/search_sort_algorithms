import sys

from .searching import binary_search, interpolation_search, linear_search
from .sorting import merge_sort


def main():
    file_t = input("Enter txt filename or path: ")
    try:
        find_sort(file_t)
    except (EOFError, KeyboardInterrupt):
        print()

def find_sort(filename):
    try:
        lst = file_toList(filename)
    except OSError as e:
        print("Could not open file:", e)
        sys.exit(1)
    except ValueError:
        print("The file must contain one integer per line!")
        sys.exit(1)

    while True:
        print(" \nChoose an option\n 1)Merge Sort\n 2)Linear Search\n 3)Binary Search\n 4)Interpolation Search\n 0)EXIT\n")
        choice = input("Enter your option's number: ").strip()

        if choice == "1":
            print("The sorted list is", preview(merge_sort(lst)))
        elif choice == "2":
            number = read_number()
            print("Starting Linear Search for number", number, "in list", preview(lst))
            index = linear_search(lst, number)
            if index != -1:
                print("Number found at index ", index)
            else:
                print("Number not found!")
        elif choice == "3":
            number = read_number()
            sorted_lst = merge_sort(lst)
            print("Starting Binary Search for number", number, "in sorted list", preview(sorted_lst))
            index = binary_search(sorted_lst, number)
            if index != -1:
                print("Number found at index ", index)
            else:
                print("Number not found!")
        elif choice == "4":
            number = read_number()
            sorted_lst = merge_sort(lst)
            print("Starting Interpolation Search for number", number, "in sorted list", preview(sorted_lst))
            index = interpolation_search(sorted_lst, number)
            if index != -1:
                print("Number found at index ", index)
            else:
                print("Number not found!")
        elif choice == "0":
            return
        else:
            print("Try again, choice", choice, "doesn't exist!")

def read_number():
    while True:
        try:
            return int(input("Enter the number you want to find its index: "))
        except ValueError:
            print("Please enter a whole number!")

def preview(plst, size=10):
    # long lists are shortened so the terminal isn't flooded
    if len(plst) <= 2 * size:
        return str(plst)
    return "[{}, ..., {}] ({} numbers)".format(
        ", ".join(map(str, plst[:size])), ", ".join(map(str, plst[-size:])), len(plst))

def file_toList(ftl):
    with open(ftl) as f:
        ilist = f.read().split()
        ilist = [int(i) for i in ilist]

    return ilist
