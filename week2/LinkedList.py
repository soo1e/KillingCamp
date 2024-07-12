class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

first.next = second
second.next = third
third.next = fourth


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            ptr = self.head
            while(ptr.next):
                ptr = ptr.next
            ptr.next = self.current = new_node
