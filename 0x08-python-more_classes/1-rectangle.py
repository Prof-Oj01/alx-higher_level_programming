#!/usr/bin/python3

class Rectangle:
   """
   Represents a rectangle with width and height properties.
   """

   def __init__(self, width=0, height=0):
       """
       Initializes a new Rectangle instance.

       Args:
           width (int): The width of the rectangle. Defaults to 0.
           height (int): The height of the rectangle. Defaults to 0.

       Raises:
           TypeError: If width or height is not an integer.
           ValueError: If width or height is negative.
       """
       self._validate_dimension("width", width)
       self._width = width
       self._validate_dimension("height", height)
       self._height = height

   @property
   def width(self):
       """
       Retrieves the width of the rectangle.

       Returns:
           int: The width of the rectangle.
       """
       return self._width

   @width.setter
   def width(self, value):
       """
       Sets the width of the rectangle.

       Args:
           value (int): The new width of the rectangle.

       Raises:
           TypeError: If value is not an integer.
           ValueError: If value is negative.
       """
       self._validate_dimension("width", value)
       self._width = value

   @property
   def height(self):
       """
       Retrieves the height of the rectangle.

       Returns:
           int: The height of the rectangle.
       """
       return self._height

   @height.setter
   def height(self, value):
       """
       Sets the height of the rectangle.

       Args:
           value (int): The new height of the rectangle.

       Raises:
           TypeError: If value is not an integer.
           ValueError: If value is negative.
       """
       self._validate_dimension("height", value)
       self._height = value

   def _validate_dimension(self, name, value):
       """
       Validates a dimension value.

       Args:
           name (str): The name of the dimension (e.g., "width", "height").
           value: The value to validate.

       Raises:
           TypeError: If value is not an integer.
           ValueError: If value is negative.
       """
       if not isinstance(value, int):
           raise TypeError(f"{name} must be an integer")
       if value < 0:
           raise ValueError(f"{name} must be >= 0")

