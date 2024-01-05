#!/usr/bin/python3
class Rectangle:
    """Represents a rectangle with width and height properties."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance."""
        self._width = width
        self._height = height

    # ... (width and height properties as defined in previous code)

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle using '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Returns a detailed string representation of the rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"

    def __print__(self):
        """Prints the rectangle using '#' characters."""
        print(self)

