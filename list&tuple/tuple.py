my_tuple = (1, 2, 'apple', 'banana')
first_element = my_tuple[0]  # Access the first element (1)
tuple_length = len(my_tuple)  # Length of the tuple (4)
second_element = my_tuple[1]  # Access the second element (2)
coordinates = (3, 4)
x, y = coordinates  # Unpack the tuple into x and y (x=3, y=4)
def get_coordinates():
    return (3, 4)
x, y = get_coordinates()  # Unpack the returned tuple (x=3, y=4)