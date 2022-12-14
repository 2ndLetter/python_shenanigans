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
        # Else statement if the number does NOT equal 1
        else:
            # Declare array_sum as zero to reset the counter
            array_sum = 0
        # Append value of array_sum to the num_list list
        num_list.append(array_sum)

    # f-String using the max() function to return the maximum value found in num_list
    print(f"Sum of max consecutive 1s is {(max(num_list))}")

# Declare my_array as an array
my_array = [1, 0, 1, 1, 0, 1, 1, 1]

# Call the my_funct function
my_funct(my_array)
