#!/usr/bin/python3

def my_funct(array):
    """Function finding sum of max consecutive 1s."""
    # Declare num_list as empty list
    num_list = []
    # Declare array_sum as zero
    array_sum = 0

    # For Loop for each number in the array
    for num in array:
        # If statement when the number equals 1
        if num == 1:
            # Add 1 to array_sum
            array_sum += 1
        # Else If statement if the number does NOT equal 1
        elif num != 1:
            # Declare array_sum as zero to reset the counter
            array_sum = 0
        # Append value of array_sum to the num_list list
        num_list.append(array_sum)

    # f-String to show the answer
    print(f"Sum of max consecutive 1s is {(max(num_list))}")

# Declare my_array within an array
my_array = [1, 0, 1, 1, 0, 1, 1, 1]

# Call the my_funct function
my_funct(my_array)
