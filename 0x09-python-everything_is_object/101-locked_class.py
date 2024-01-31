#!/usr/bin/python3
"""This module defines class LockedClass"""


class LockedClass:
    """
    LockedClass: Prevents dynamic creation of new instance attributes,
    except for 'first_name'.
    """

    __slots__ = ['first_name']
