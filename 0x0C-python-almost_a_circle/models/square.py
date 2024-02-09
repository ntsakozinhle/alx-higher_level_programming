#!/usr/bin/python3
"""Module that defines class Square and inherits from Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance with size, x, y, and id"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width if self.width == self.height else self.height)
