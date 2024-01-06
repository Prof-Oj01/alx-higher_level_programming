#!/usr/bin/python3
class LockedClass:
    __slots__ = ('first_name',)  # Restrict allowed attributes

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")  # Use f-string for dynamic attribute name
        super().__setattr__(name, value)  # Call superclass method to set allowed attribute

