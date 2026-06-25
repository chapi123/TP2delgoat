class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SingleLink:
    def __init__ (self, values=None):
        if values:
            nodes = [Node(value) for value in values]

            for i in range(len(nodes)-1):
                nodes[i].next = nodes[i+1]

            self.head = nodes[0]
            self.tail = nodes[-1]
        else:
            self.head = None
            self.tail = None

    def print_values (self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def iscycled (self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False

    def get_index_value (self, index):
        current = self.head
        if current != None:
            for _ in range(index):
                if current != None:
                    current = current.next
                else: raise IndexError('no index')
            return current
        return False
    
    def get_item (self, value):
        current = self.head
        while current != None:
            if current.data == value:
                return current
            current = current.next
        return False

    def add_node(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def count_nodes(self):
        current = self.head
        nodes = 0
        while current is not None:
            current = current.next
            nodes += 1
        return nodes

    def sort_nodes(self):
        changed = True
        while changed:
            current = self.head
            changed = False
            while current is not None and current.next is not None:
                if current.data > current.next.data :
                    current.data, current.next.data = current.next.data, current.data
                    changed = True         
                current = current.next

    def invert_nodes(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def isEmpty(self):
        return self.head == None
    
    def delete(self, data):
        if self.head is None:
            raise IndexError("empty")

        if self.head.data == data:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return True

        prev_node = self.head
        current = self.head.next

        while current is not None:
            if current.data == data:
                prev_node.next = current.next

                if current == self.tail:
                    self.tail = prev_node

                return True

            prev_node = current
            current = current.next

        return False

    def insert(self, data, prev):
        new_node = Node(data)
        prev_node = self.get_item(prev)

        if prev_node == False:
            return False

        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node

        if prev_node == self.tail:
            self.tail = new_node