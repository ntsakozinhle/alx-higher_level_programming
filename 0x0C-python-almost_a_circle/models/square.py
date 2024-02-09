#!/usr/bin/python3
"""Module that defines class Square and inherits from Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance with size, x, y, and id"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        self.width = value
        self.height = value
