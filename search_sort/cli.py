"""Interactive menu: generates random lists and runs the algorithms on them."""

import random

from . import benchmark
from .searching import binary_search, interpolation_search, linear_search
from .sorting import merge_sort, quick_sort

DEFAULT_SIZE = 100000
MAX_SIZE = 1000000  # bigger lists make sorting slow enough to look stuck
MAX_VALUE = 1000000

MENU = """
Choose an option
 1)Merge Sort
 2)Quick Sort
 3)Linear Search
 4)Binary Search
 5)Interpolation Search
 6)Generate a new random list
 7)Benchmark all algorithms
 0)EXIT
"""

SORTED_SEARCHES = {
    "4": ("Binary Search", binary_search),
    "5": ("Interpolation Search", interpolation_search),
}


def main():
    try:
        menu()
    except (EOFError, KeyboardInterrupt):
        print()


def menu():
    numbers = new_random_list()
    ordered = None  # sorted copy, reused by the searches until a new list is generated

    while True:
        print(MENU)
        choice = input("Enter your option's number: ").strip()

        if choice == "1":
            ordered = merge_sort(numbers)
            print("The sorted list is", preview(ordered))
        elif choice == "2":
            ordered = quick_sort(numbers)
            print("The sorted list is", preview(ordered))
        elif choice == "3":
            target = read_number()
            print(f"Starting Linear Search for number {target} in list {preview(numbers)}")
            report(linear_search(numbers, target))
        elif choice in SORTED_SEARCHES:
            name, search = SORTED_SEARCHES[choice]
            target = read_number()
            if ordered is None:
                ordered = merge_sort(numbers)
            print(f"Starting {name} for number {target} in sorted list {preview(ordered)}")
            report(search(ordered, target))
        elif choice == "6":
            numbers = new_random_list()
            ordered = None
        elif choice == "7":
            print("Timing every algorithm, this takes a few seconds...")
            print(benchmark.format_table(benchmark.run()))
        elif choice == "0":
            return
        else:
            print(f"Try again, choice {choice} doesn't exist!")


def report(index):
    """Print where a search found the number, or that it found nothing."""
    if index == -1:
        print("Number not found!")
    else:
        print(f"Number found at index {index}")


def new_random_list():
    """Ask for a size, generate that many random numbers and describe them."""
    size = read_size()
    numbers = random_list(size)
    print(f"Generated {size} random numbers between 0 and {MAX_VALUE}: {preview(numbers)}")
    if numbers:
        print("For example, try searching for", random.choice(numbers))
    return numbers


def random_list(size, max_value=MAX_VALUE):
    return [random.randint(0, max_value) for _ in range(size)]


def read_size():
    """Ask how many numbers to generate until the answer is a size we can handle."""
    while True:
        answer = input(
            f"How many random numbers, up to {MAX_SIZE}? (press Enter for {DEFAULT_SIZE}): "
        ).strip()
        if answer == "":
            return DEFAULT_SIZE
        try:
            size = int(answer)
        except ValueError:
            print(f"Please enter a whole number from 0 to {MAX_SIZE}!")
            continue
        if 0 <= size <= MAX_SIZE:
            return size
        print(f"Please enter a whole number from 0 to {MAX_SIZE}!")


def read_number():
    """Ask for the number to search for until the answer is a whole number."""
    while True:
        try:
            return int(input("Enter the number you want to find its index: "))
        except ValueError:
            print("Please enter a whole number!")


def preview(items, size=10):
    """Show short lists in full and long ones as their first and last numbers.

    Keeps the terminal readable when the list has thousands of numbers.
    """
    if len(items) <= 2 * size:
        return str(list(items))
    head = ", ".join(map(str, items[:size]))
    tail = ", ".join(map(str, items[-size:]))
    return f"[{head}, ..., {tail}] ({len(items)} numbers)"
