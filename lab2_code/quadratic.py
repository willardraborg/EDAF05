class QuadraticProbe():
    def __init__(self, size=2):
        self.keys = [None] * size
        #self.values = [None] * size
        self.values = [0] * size
        self.size = size
        self.pairs = 0
        self.maxLoad = 0.3
        self.minLoad = 0.1


    def nextPrime(self, n):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        for p in range(n + 1, 2 * n):
            if is_prime(p):
                return p

        return None

    def resize(self):
        factor = 0
        tempKeys = self.keys
        tempValues = self.values
        load = self.pairs / self.size

        #self.size = self.size * 2 if load > self.maxLoad else self.size // 2
        self.size = self.nextPrime(self.size << 1) if load > self.maxLoad else self.nextPrime(self.size >> 1)
        if(self.size == 0):
            self.size = 2

        self.values = [0] * self.size
        self.keys = [None] * self.size
        
        for index in range(len(tempKeys)):
            if tempKeys[index] is not None and tempKeys[index] != "DELETED":
                self.set(tempKeys[index], tempValues[index])
    
    def set(self, key, value):
        i = 1
        index = hash(key) % self.size

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + i**2) % self.size
            i += 1

        self.keys[index] = key
        self.values[index] = value

    
    def add(self, key, value):
        i = 1
        self.pairs = self.pairs + 1

        load = self.pairs / self.size
        
        if load > self.maxLoad:
            self.resize()
        
        index = hash(key) % self.size

        if self.keys[index] is None or self.keys[index] == "DELETED":
            self.keys[index] = key
            self.values[index] = value
        else:
            
            while self.keys[index] is not None and self.keys[index] != "DELETED":
                index = (index + i**2) % self.size
                i += 1
            self.keys[index] = key
            self.values[index] = value


    def getKeys(self):
        return self.keys

    def getValues(self):
        return self.values
        
    def get(self, key):
        i = 1
        index = hash(key) % self.size
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + i**2) % self.size
            i += 1
        
        return None

    def contains(self, key):
        i = 1
        index = hash(key) % self.size

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return True
            index = (index + i**2) % self.size
            i += 1
        return False

    def delete(self, key):
        i = 1
        index = hash(key) % self.size
        while self.keys[index] is not None: 
            if self.keys[index] == key: 
                self.keys[index] = "DELETED"
                self.values[index] = 0
                self.pairs -= 1
                load = self.pairs / self.size
                if load < self.minLoad:
                    self.resize()
                return
            index = (index + i**2) % self.size
            i += 1

    # def delete2(self, key):
    #     i = 1
    #     index = hash(key) % self.size
        
    #     while self.keys[index] is not None:
    #         if self.keys[index] == key:
    #             self.keys[index] = None
    #             self.values[index] = 0
    #             self.pairs -= 1
                
    #             next_index = (index + i**2) % self.size
    #             i += 1
    #             while self.keys[next_index] is not None:
    #                 temp_key = self.keys[next_index]
    #                 temp_value = self.values[next_index]
                    
    #                 self.keys[next_index] = None
    #                 self.values[next_index] = 0

    #                 self.set(temp_key, temp_value)

    #                 next_index = (next_index + i**2) % self.size
    #                 i += 1
    #             load = self.pairs / self.size
    #             if load < self.minLoad:
    #                 self.resize()
                
    #             return
    #         index = (index + i**2) % self.size
    #         i += 1



