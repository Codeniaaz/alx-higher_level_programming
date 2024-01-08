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
            raise ValueError("{} must be greater than 0".format(name))
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
