class Node:
    def __init__(self, k, v):
        self.key   = k
        self.value = v
        self.next  = None

class LinkedList:
    def __init__(self, n=None):
        self.head = n
    
    def add(self, key, value):
        n = Node(key, value)

        if not self.head:
            self.head = n 
        else:
            n.next = self.head
            self.head = n
    
    def set(self, key, value):
        temp = self.head
        while temp is not None:
            if temp.key == key:  
                temp.value = value
                return
            temp = temp.next

        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node


    def contains(self, key):
        current = self.head
        while current: 
            if current.key == key:
                return True
            current = current.next
        return False

    def get(self, key):
        temp = self.head
        while temp is not None and temp.key != key:  # Use != instead of "is not", is not is object identity whereas != checks value
            temp = temp.next
        return None if temp is None else temp.value  # Return the value if found
        
    def remove(self, key):
        temp = self.head
        prev = None

        while temp is not None and temp.key != key:
            prev = temp
            temp = temp.next

        if temp is None:  # Key not found
            return

        if prev is None:  # The key is in the head node
            self.head = temp.next
        else:  # Bypass the node to remove it
            prev.next = temp.next

    
    def keys(self):
        """Returns a list of all keys in the linked list."""
        result = []
        current = self.head
        while current:
            result.append(current.key)
            current = current.next
        return result

    def values(self):
        """Returns a list of all values in the linked list."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
        

class SeparateChain:
    def __init__(self, size=1):
        self.table = [None] * size  # Initialize hash table slots
        self.size = size
        self.pairs = 0
        self.maxLoad = 10
        self.minLoad = 0.1

    def resize(self):
        factor = 0
        temp = self.table
        load = self.pairs / self.size
        self.size = self.size << 1 if load > self.maxLoad else self.size >> 1
        if(self.size == 0):
            self.size = 1
        self.table = [None] * self.size
        for chain in temp:
            if chain:
                current = chain.head
                while current:
                    self.set(current.key, current.value)
                    current = current.next

    def get(self, key):
        #index = hash(key) % self.size
        index = hash(key) & (self.size - 1)
        chain = self.table[index]
        if chain:
            return chain.get(key)
        return None  # Return None if key is not found

    def remove(self, key):
        index = hash(key) & (self.size - 1)
        self.table[index].remove(key)
        self.pairs = self.pairs - 1
        load = self.pairs / self.size
        if load < self.minLoad:
            self.resize()
        #potentiellt minska array

    def add(self, key, value):
        # load = pairs / size, should be 1
        self.pairs = self.pairs + 1
        load = self.pairs / self.size
        if load > self.maxLoad:
            self.resize()
        index = hash(key) & (self.size - 1)
        if self.table[index]:  
            self.table[index].add(key, value)
        else: 
            self.table[index] = LinkedList()
            self.table[index].add(key, value)

    def contains(self, key): 
        index = hash(key) & (self.size - 1)
        chain = self.table[index]
        return chain is not None and chain.contains(key)

    def set(self, key, value):
        index = hash(key) & (self.size - 1) 

        if self.table[index]:  
            self.table[index].set(key, value)
        else: 
            self.table[index] = LinkedList()
            self.table[index].set(key, value)

    def keys(self):
        """Returns a list of all keys stored in the hash table."""
        all_keys = []
        for chain in self.table:
            if chain:
                all_keys.extend(chain.keys())
        return all_keys

    def values(self):
        """Returns a list of all values stored in the hash table."""
        all_values = []
        for chain in self.table:
            if chain:
                all_values.extend(chain.values())  # Get all values from the linked list
        return all_values