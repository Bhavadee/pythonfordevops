my_list = [1, 2, 3, 'apple', 'banana']
first_element = my_list[0] 
list_length = len(my_list)  # Length of the list (5)
my_list.append(4)  # Adds 4 to the end of the list
my_list.remove('apple')  # Removes 'apple' from the list
subset = my_list[1:4]  # Creates a new list with elements at index 1, 2, and 3
new_list = my_list + [5, 6]  # Concatenates my_list with [5, 6]
is_present = 'banana' in my_list  # Checks if 'banana' is in the list (True)
print(my_list)
print(subset)