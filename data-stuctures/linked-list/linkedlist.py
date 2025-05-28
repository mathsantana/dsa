#!/usr/bin/env python3

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class EmptyListNode(LinkedListNode):
    def __init__(self):
        super().__init__(None)
        
class LinkedList:
    def __init__(self):
        self.first = EmptyListNode()

    def addFirst(self, value):
        node = LinkedListNode(value)
        node.next = self.first
        self.first = node

    def isEmpty(self):
        return isinstance(self.first, EmptyListNode)

    def addLast(self, value):
        node = LinkedListNode(value)
        n = self.first

        if self.isEmpty():
            node.next = self.first
            self.first = node
        else:
            while True:
                if (isinstance(n.next, EmptyListNode)):
                    node.next = n.next
                    n.next = node
                    break
                n = n.next

    def pop(self):
        if (self.isEmpty()):
            raise ReferenceError("List is empty!")
        
        node = self.first
        self.first = self.first.next

        return node.value

        
    def __str__(self):
        node = self.first
        i = 0
        result = []

        while True:
            if isinstance(node, EmptyListNode):
                if (self.isEmpty()):
                    return "EMPTY"
                break
            result.append(f"{i}: {node.value}")
            i += 1
            node = node.next
            
        return " | ".join(result)


if __name__ == "__main__":
    lst = LinkedList()
    print(lst)
    lst.addFirst("Matheus")
    print(lst)
    lst.addFirst("Catarina")
    print(lst)
    lst.addLast("Stephane")
    print(lst)
    lst.pop()
    print(lst)
    
