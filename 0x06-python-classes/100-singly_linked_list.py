#!/usr/bin/python3
"""
Define a class Node that defines a node of a singly linked list.
"""
class Node:
    """Represents a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """
        Initializes a new node.

        Args:
            data (int): The data for the new node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next node of the current node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""
Define a class SinglyLinkedList that defines a singly linked list.
"""
class SinglyLinkedList:
    """Represents a singly linked list."""
    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
