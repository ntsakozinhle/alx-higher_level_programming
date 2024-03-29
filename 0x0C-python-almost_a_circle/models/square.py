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

    def to_dictionary(self):
        """Returns the dictionary representation of the Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """Assign attributes to the instance"""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for idx, arg in enumerate(args):
                setattr(self, attrs[idx], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
