from linked_list import SingleLink

class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [SingleLink() for _ in range(size)]

    def hash(self, key):
        total = 0
        for char in str(key):
            total += ord(char)
        return total

    def get_index(self, key):
        return self.hash(key) % self.size

    def put(self, key, value):
        index = self.get_index(key)
        bucket = self.buckets[index]

        current = bucket.head

        while current is not None:
            if current.data[0] == key:
                return False

            current = current.next

        bucket.add_node((key, value))
        return True

    def get(self, key):
        index = self.get_index(key)
        bucket = self.buckets[index]

        current = bucket.head

        while current is not None:
            if current.data[0] == key:
                return current.data[1]
            current = current.next

        return None

    def remove(self, key):
        index = self.get_index(key)
        bucket = self.buckets[index]

        current = bucket.head

        while current is not None:
            if current.data[0] == key:
                return bucket.delete(current.data)
            current = current.next

        return False

    def print_map(self):
        for i, bucket in enumerate(self.buckets):

            current = bucket.head

            while current is not None:
                key, value = current.data
                print(f"  {key}: {value}")
                current = current.next
    
    def values(self):
        values = []

        for bucket in self.buckets:
            current = bucket.head

            while current is not None:
                values.append(current.data[1])
                current = current.next

        return values

class HashSet:
    def __init__(self, size):
        self.size = size
        self.buckets = [SingleLink() for _ in range(size)]

    def hash(self, data):
        total = 0
        for char in str(data):
            total += ord(char)
        return total

    def get_index(self, key):
        return key % self.size

    def put(self, data):
        if self.get(data):
            return False

        index = self.get_index(self.hash(data))
        self.buckets[index].add_node(data)
        return True

    def get(self, data):
        index = self.get_index(self.hash(data))
        bucket = self.buckets[index]

        current = bucket.head

        while current is not None:
            if current.data == data:
                return current.data
            current = current.next

        return None

    def remove(self, data):
        index = self.get_index(self.hash(data))
        bucket = self.buckets[index]
        bucket.data

    def print_set(self):
        for i, bucket in enumerate(self.buckets):
            bucket.print_values(i)