#!/usr/bin/python3
""" This module defines the class Rectangle """


class Rectangle:
    """
    Class that defines a rectangle

    Attributes:
        - width (int): width of the rectangle
        - height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes an instance of the Rectangle class.

        Parameters:
            - width (int): width of the rectangle (default is 0)
            - height (int): height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle

        Parameters:
            value (int): new width value.

        Raises:
            TypeError: if the width is not an integer
            ValueError: if the width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the retrieving the height of the rectangle

        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle

        Parameters:
            value (int): new height value

        Raises:
            TypeError: if the height is not an integer
            ValuseError: if the height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public instance method that retursn the rectangle area

        Returns:
            int: Area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method returns the perimeter

        Returns:
            int: Perimeter of the rectangle (2 * (width + height))
        """
        return 2 * (self.__width + self.__height) if self.__width != 0 and self.__height != 0 else 0
