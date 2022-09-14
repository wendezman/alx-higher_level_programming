#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    def __init__(self) -> None:
        self.__head = None

    def __str__(self) -> str:
        output = list()
        future = self.__head

        while future is not None:
            output.append(str(future.data))
            future = future.next_node

        return "\n".join(output)

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
            return

        if value < self.__head.data:
            self.__head = Node(value, self.__head)
            return

        future, past = self.__head.next_node, self.__head
        while future is not None:
            if value < future.data:
                past.next_node = Node(value, future)
                return
            past = future
            future = future.next_node
        past.next_node = Node(value)
