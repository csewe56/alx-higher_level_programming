#!/usr/bin/python3
"""
Define a class Square that defines a square.
"""
class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (number): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Override the equality operator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Override the inequality operator."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Override the greater than operator."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Override the greater than or equal operator."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Override the less than operator."""
        return self.area() < other.area()

    def __le__(self, other):
        """Override the less than or equal operator."""
        return self.area() <= other.area()
