class Node:
    def __init__(self, value, next_node=None):
        self.defvalue = value
        self.nextnode = next_node

    def value(self):
        return self.defvalue

    def next(self):
        return self.nextnode


class LinkedList:
    def __init__(self, values=None):
        self.hdold = None
        self.hdprev = None
        self.hd = None
        self.tail = None
        if values is not None:
            for i in values:
                self.push(i)

    def __len__(self):
        count = 0
        node = self.hd
        while node:
            count += 1
            node = node.nextnode
        return count

    def head(self):
        if self.hd == None:
            raise EmptyListException("The list is empty.")
        return self.hd

    def push(self, value):
        if self.hd is None:
            self.tail = self.hd = Node(value)
        else:
            self.hdprev = self.hd
            self.hd = Node(value)
            self.hd.nextnode = self.hdprev

    def pop(self):
        self.hdold = self.hd
        if self.hd is None:
            raise EmptyListException("The list is empty.")
        self.hd = self.hd.nextnode
        return self.hdold.value()

    def __iter__(self):
        node = self.hd
        while node:
            yield node.value()
            node = node.nextnode

    def reversed(self):
        reversed_list = []
        for i in self:
            reversed_list.insert(0, i)
        while reversed_list:
            yield reversed_list[0]
            reversed_list.pop(0)


class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message
