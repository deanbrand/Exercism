class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.next = succeeding
        self.prev = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def _check_size(self):
        if self.size == 0:
            raise IndexError("List is empty")

    def unshift(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            node = Node(value, self.head)
            self.head.prev = node
            self.head = node
        self.size += 1

    def shift(self):
        self._check_size()
        self.size -= 1
        val = self.head.value
        if self.size == 0:
            self.head = self.tail = None
            return val
        self.head = self.head.next
        self.head.prev = None
        return val

    def push(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            tail = Node(value, None, self.tail)
            self.tail.next = tail
            self.tail = tail
        self.size += 1

    def pop(self):
        self._check_size()
        self.size -= 1
        val = self.tail.value
        if self.size == 0:
            self.head = self.tail = None
            return val
        self.tail = self.tail.prev
        self.tail.next = None
        return val

    def delete(self, value):
        if self.size < 1:
            raise ValueError("Value not found")
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.size -= 1
        else:
            prev = self.head
            curr = prev.next
            while curr:
                if curr.value == value:
                    prev.next = curr.next
                    curr.next.prev = prev
                    self.size -= 1
                    break
                else:
                    prev = curr
                    curr = prev.next
            if curr is None:
                raise ValueError("Value not found")
