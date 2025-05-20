#!/usr/bin/env python3

# Created By: Luke Di Bert
# Date: May 20, 2025

# adds random module
import random


def max_value(array):
    max_value = 0
    for counter in range(0, len(array)):
        if array[counter] > max_value:
            max_value = array[counter]
    return max_value


def main():
    rand_num_array = []
    for counter in range(0, 10):
        rand_num_array.append(random.randint(0, 100))
        print(rand_num_array[counter], "was added to the array")
    max_num = max_value(rand_num_array)
    print("The max value is", max_num)


if __name__ == "__main__":
    main()
