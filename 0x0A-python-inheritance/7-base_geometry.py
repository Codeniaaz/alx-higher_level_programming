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
            raise ValueError("<name> must be greater than 0")
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
