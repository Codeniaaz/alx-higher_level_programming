#!/usr/bin/python3
"""Defines a function that prints names.

This script defines a function 'say_my_name' that takes a 'first_name' and an optional 'last_name'
(defaults to an empty string) as parameters. It then checks if both parameters are strings and prints
the formatted full name. If any parameter is not a string, it raises a TypeError.

Example:
    say_my_name("John", "Doe")  # Output: "My name is John Doe"
"""

def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")

