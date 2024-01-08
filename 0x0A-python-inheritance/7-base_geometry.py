#!/usr/bin/python3
"""An class that has a public method"""


class BaseGeometry:
    ''' it has a public method'''
    def area(self):
        ''' that raises an Exception with a message'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''def integer_validator(self, name, value)'''

        if value <= 0:
            raise ValueError(f"{value} must be greater than 0")
        if type(value) is not int:
            raise TypeError(f"{value} must be an integer")
