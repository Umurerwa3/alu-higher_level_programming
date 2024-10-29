#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")  # Print element without new line
            count += 1                 # Increment count for each printed element
        except IndexError:
            break                      # Stop if i is out of range
    print()  # Add a new line after printing elements
    return count  # Return the actual number of elements printed
   