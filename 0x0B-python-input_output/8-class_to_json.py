#!/usr/bin/python3
"""Module for converting a class instance to a dictionary representaion."""


def class_to_json(obj):
    """
    Convert an instance of a class to a dictionary representation.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the class instance.
    """
    attributes = obj.__dict__

    public_attributes = {key: value for key, value in attributes.items() if  not key.startswith('__')}
    for key, value in public_attributes.items():
        if isinstance(value, MyClass):
            public_attributes[key] = class_to_json(value)

    return public_attributes


class MyClass:
    """My class"""

    def __init__(self, name, number=0):
        self.name = name
        self.number = number

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)


if __name__ == "__main__":
    m = MyClass("John", 89)
    print(type(m))
    print(m)

    mj = class_to json(m)
    print(type(mj))
    print(mj)
