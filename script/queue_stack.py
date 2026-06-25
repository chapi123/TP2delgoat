from script.linked_list import SingleLink

class Stack:
    def __init__(self, values=None):
        if values:
            self.instance = SingleLink(values)
        else:
            self.instance = SingleLink()

    def push(self,data):
        self.instance.add_node(data)
    
    def pop(self):
        if self.instance.head is None:
            raise IndexError("empty stack")

        if self.instance.head.next == None:
            popped = self.instance.head
            self.instance.head = None
            self.instance.tail = None
            return popped.data

        current = self.instance.head
        popped = current.next
        while current.next != self.instance.tail:
            current = current.next
            popped = current.next
        
        self.instance.tail = current
        current.next = None

        return popped.data
    
    def peek(self):
        if self.instance.head == None:
            return None
        return self.instance.tail.data
    
    def isEmpty(self):
        return self.instance.head == None
    
    def size(self):
        return self.instance.count_nodes()
    
class Queue:
    def __init__(self, values=None):
        if values:
            self.instance = SingleLink(values)
        else:
            self.instance = SingleLink()

    def enqueue(self,data):
        self.instance.add_node(data)
    
    def dequeue(self):
        if self.instance.head is None:
            return None

        value = self.instance.head.data
        self.instance.head = self.instance.head.next

        if self.instance.head is None:
            self.instance.tail = None

        return value
    
    def peek(self):
        if self.instance.head == None:
            return None
        return self.instance.head.data
    
    def isEmpty(self):
        return self.instance.head == None
    
    def size(self):
        return self.instance.count_nodes()