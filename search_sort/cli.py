import random

from .searching import binary_search, interpolation_search, linear_search
from .sorting import merge_sort

DEFAULT_SIZE = 100000
MAX_VALUE = 1000000


def main():
    try:
        find_sort()
    except (EOFError, KeyboardInterrupt):
        print()

def find_sort():
    lst = new_random_list()

    while True:
        print(" \nChoose an option\n 1)Merge Sort\n 2)Linear Search\n 3)Binary Search\n 4)Interpolation Search\n 5)Generate a new random list\n 0)EXIT\n")
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
        elif choice == "5":
            lst = new_random_list()
        elif choice == "0":
            return
        else:
            print("Try again, choice", choice, "doesn't exist!")

def new_random_list():
    size = read_size()
    lst = random_list(size)
    print("Generated {} random numbers between 0 and {}: {}".format(size, MAX_VALUE, preview(lst)))
    if lst:
        print("For example, try searching for", random.choice(lst))
    return lst

def random_list(size, max_value=MAX_VALUE):
    return [random.randint(0, max_value) for _ in range(size)]

def read_size():
    while True:
        answer = input("How many random numbers? (press Enter for {}): ".format(DEFAULT_SIZE)).strip()
        if answer == "":
            return DEFAULT_SIZE
        try:
            size = int(answer)
        except ValueError:
            size = -1
        if size >= 0:
            return size
        print("Please enter a whole number of 0 or more!")

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
