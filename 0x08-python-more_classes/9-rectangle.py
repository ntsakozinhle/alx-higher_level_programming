#!/usr/bin/python3
""" This module defines class Rectangle """


class Rectangle:
    """
    Class that defines a rectangle.

    Attributes:
        - width (int): width of the rectangle.
        - height (int): height of the rectangle.
        - number_of_instances (int): class attribute to keep track of the
        number of instances.
        - print_symbol: Class attribute representing the symbol for string representation.

    Methods:
        - __init__(self, width=0, height=0): Initializes an instance of the rectangle class.
        - area(self): Public instance method that returns the rectangle area.
        - perimeter(self): Public instance method that returns the rectangle perimeter.
        - __str__(self): Returns a string representation of the rectangle using '#'.
        - __repr__(self): Returns a string representation of the rectangle.
        - __del__(self): Deletes an instance of Rectangle and prints a farewell message.
        - bigger_or_equal(rect_1, rect_2): Static method that returns the
        biggest rectangle based the area.
        - square(cls, size=0): Class method that returns a new Rectangle
        instance with width == height == size.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes an instance of the rectangle class.

        Parameters:
            - width (int): width of the rectangle (default is 0).
            - height (int): height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        Returns:
            int: width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.

        Parameters:
            value (int): new width value.

        Raises:
            TypeError: if the width is not an integer.
            ValueError: if the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.

        Returns:
            int: height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.

        Parameters:
            value (int): new height value.

        Raises:
            TypeError: if the height is not an integer.
            ValueError: if the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public instance method that returns the area.

        Returns:
            int: Area of rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method that returns the rectangle perimeter.

        Returns:
            int: Perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.__width + self.__height) if self.__width != 0 and self.__height != 0 else 0

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'.

        Returns:
            str: string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(Rectangle.print_symbol) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle to recreate a new
            instance using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes an instance of Rectangle and prints a farewell message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest rectangle based on the area.

        Parameters:
            - rect_1 (Rectangle): first rectangle.
            - rect_2 (Rectangle): second rectangle.

        Raises:
            TypeError: If rect_1 is not an instance of Rectangle.
            TypeError: If rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the larger or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
        Class method that returns a new Rectangle instance with width == height
        == size.

        Parameters:
            Rectangle: A new Rectangle instance representing a square.
        """
        return cls(size, size)
