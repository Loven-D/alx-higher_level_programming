#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Create an empty set to store elements present in only one set
    diff_set = set()
    
    # Iterate over the elements in the first set
    for item in set_1:
        # Check if the element is not in the second set
        if item not in set_2:
            diff_set.add(item)
    
    # Iterate over the elements in the second set
    for item in set_2:
        # Check if the element is not in the first set
        if item not in set_1:
            diff_set.add(item)
    
    return diff_set
