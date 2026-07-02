from script.linked_list import SingleLink

class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [SingleLink() for _ in range(size)]

    def get_index(self, key):
        return hash(key) % self.size

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
    
    def keys(self):
        keys = []

        for bucket in self.buckets:
            current = bucket.head

            while current:
                keys.append(current.data[0])
                current = current.next

        return keys
    
    def search_pokemon_by_id(pokedex, target):
        ids = pokedex.keys()
        ids.sort()

        left = 0
        right = len(ids) - 1

        while left <= right:
            mid = (left + right) // 2

            if ids[mid] == target:
                return pokedex.get(target)

            elif ids[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return None

class HashSet:
    def __init__(self, size):
        self.size = size
        self.buckets = [SingleLink() for _ in range(size)]

    def get_index(self, key):
        return key % self.size

    def put(self, data):
        if self.get(data):
            return False

        index = self.get_index(hash(data))
        self.buckets[index].add_node(data)
        return True

    def get(self, data):
        index = self.get_index(hash(data))
        bucket = self.buckets[index]

        current = bucket.head

        while current is not None:
            if current.data == data:
                return current.data
            current = current.next

        return None

    def remove(self, data):
        index = self.get_index(hash(data))
        return self.buckets[index].delete(data)

    def print_set(self):
        for i, bucket in enumerate(self.buckets):
            bucket.print_values()

    def values(self):
        values = []

        for bucket in self.buckets:
            current = bucket.head

            while current is not None:
                values.append(current.data)
                current = current.next

        return values