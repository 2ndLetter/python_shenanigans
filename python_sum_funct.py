#!/usr/bin/python3

def my_funct(array):
    """Function finding sum of max consecutive 1s."""
    num_list = []
    array_sum = 0
    for num in array:
        if num == 1:
            array_sum = array_sum + 1
        elif num != 1:
            array_sum = 0
            continue
        num_list.append(array_sum)

    print(f"Sum of consecutive 1s is {(max(num_list))}")

my_array = [1, 0, 1, 1, 0, 1, 1, 1]

my_funct(my_array)
