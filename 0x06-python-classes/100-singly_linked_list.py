#!/usr/bin/python3
"""This module defines classes for a singly linked list."""


class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        __data (int): Private attribute representing the data of the node
        __next_node (Node): Private attribute representing the next node
        in the list
    """

    def __init__(self, data, next_node=None):
        """Initializes a new Node instance.

        Args:
            data (int): The data of the node.
            next_node (Node, optional): The next node in the list
            Defaults to 0
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrives the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node.

        Args:
            value (int): The new data of the node.

        Raises:
            TypeError: if the value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the list

        Args:
            value (Node): the new next node.

        Raises:
            TypeError: if the value is not a Node or None
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head: the first node in the list.
    """

    def __init__(self):
        """Initializes a new SinglyLinkedList instance."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list/

        Args:
            value (int): The value of the new Node.
        """
        new_node = Node(value)
        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Prints the entire list in stdout, one node number per line."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
