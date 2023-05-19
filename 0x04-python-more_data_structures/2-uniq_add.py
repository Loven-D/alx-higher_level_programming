#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()

    # Iterate over the elements in the input list
    for item in my_list:
        # Check if the element is an integer and add it to the set
        if isinstance(item, int):
            unique_integers.add(item)

    # Calculate the sum of the unique integers
    total = sum(unique_integers)

    return total
