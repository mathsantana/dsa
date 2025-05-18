#!/usr/bin/env python3

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class EmptyListNode(LinkedListNode):
    def __init__(self):
        super().__init__(None)
        
class LinkedList:
    def __init__(self, first = None):
        self.first = EmptyListNode() if first == None else first

    def addFirst(self, node):
        node.next = self.first
        self.first = node

    def isEmpty(self):
        return isinstance(self.first, EmptyListNode)

    def addLast(self, node):
        n = self.first

        if self.isEmpty():
            node.next = self.first
            self.first = node.next

        while True:
            if (isinstance(n.next, EmptyListNode)):
                node.next = n.next
                n.next = node
                break
            n = n.next

    def pop(self):
        if (self.isEmpty()):
            raise ReferenceError("List is empty!")
        
        self.first = self.first.next

        
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
    node = LinkedListNode("Matheus")
    lst.addFirst(node)
    print(lst)
    lst.addFirst(LinkedListNode("Catarina"))
    print(lst)
    lst.addLast(LinkedListNode("Stephane"))
    print(lst)
    lst.pop()
    print(lst)
    
