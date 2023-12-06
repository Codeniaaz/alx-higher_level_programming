Sets:

A set is an unordered collection of unique elements in Python.
Sets are defined using curly braces {}.
Duplicate elements are not allowed in a set; it only stores unique values.
Sets support various mathematical operations like union, intersection, difference, and symmetric difference.
You can add elements to a set using the add() method, and remove elements using remove() or discard().
Example:

python
Copy code
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(3)
Dictionaries:

A dictionary is an unordered collection of key-value pairs in Python.
Dictionaries are defined using curly braces {} and consist of key-value pairs separated by colons.
Keys in a dictionary must be unique, and they are usually immutable types like strings or numbers.
Values can be of any data type, including other dictionaries.
You can access, insert, or modify values in a dictionary using the associated key.
Example:

python
Copy code
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # Output: John
my_dict['age'] = 26  # Modifying the value associated with the 'age' key
In summary, sets are used for storing unique and unordered elements, while dictionaries are used for storing key-value pairs, providing a way to associate data with keys for easy retrieval.
