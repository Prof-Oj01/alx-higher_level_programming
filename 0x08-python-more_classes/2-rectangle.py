#!/usr/bin/python3
class Rectangle:
    """Represents a rectangle with width and height properties."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance."""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

