class LinearProbe():
    def __init__(self, size=1):
        self.keys = [None] * size
        self.values = [0] * size
        self.size = size
        self.pairs = 0
        self.maxLoad = 0.5
        self.minLoad = 0.1

    def resize(self):
        tempKeys = self.keys
        tempValues = self.values
        load = self.pairs / self.size

        self.size = self.size << 1 if load > self.maxLoad else self.size >> 1
        if(self.size == 0):
            self.size = 1

        self.values = [0] * self.size
        self.keys = [None] * self.size
        
        for index in range(len(tempKeys)):
            if tempKeys[index] is not None and tempKeys[index] != "DELETED":
                self.set(tempKeys[index], tempValues[index])
    
    def set(self, key, value):
        index = hash(key) & (self.size-1)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) & (self.size - 1)

        self.keys[index] = key
        self.values[index] = value

    
    def add(self, key, value):
        
        self.pairs = self.pairs + 1

        load = self.pairs / self.size
        
        if load > self.maxLoad:
            self.resize()
        
        index = hash(key) & (self.size-1)

        if self.keys[index] is None or self.keys[index] == "DELETED":
            self.keys[index] = key
            self.values[index] = value
        else:
            
            while self.keys[index] is not None and self.keys[index] != "DELETED":
                index = (index + 1) & (self.size - 1)
            self.keys[index] = key
            self.values[index] = value

    def getKeys(self):
        return self.keys

    def getValues(self):
        return self.values
        
    def get(self, key):
        index = hash(key) & (self.size-1)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) & (self.size - 1)
        
        return None

    def contains(self, key):
        index = hash(key) & (self.size-1)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return True
            index = (index + 1) & (self.size - 1)
        
        return False
    
    def delete(self, key):
        index = hash(key) & (self.size-1)
        while self.keys[index] is not None: 
            if self.keys[index] == key: 
                self.keys[index] = "DELETED"
                self.values[index] = 0
                self.pairs -= 1
                load = self.pairs / self.size
                if load < self.minLoad:
                    self.resize()
                return
            index = (index + 1) & (self.size - 1)    

    # def delete2(self, key):
    #     index = hash(key) & (self.size-1)
        
    #     while self.keys[index] is not None:
    #         if self.keys[index] == key:
    #             self.keys[index] = None
    #             self.values[index] = 0
    #             self.pairs -= 1
                
    #             next_index = (index + 1) % self.size
    #             while self.keys[next_index] is not None:
    #                 temp_key = self.keys[next_index]
    #                 temp_value = self.values[next_index]
                    
    #                 self.keys[next_index] = None
    #                 self.values[next_index] = 0

    #                 self.set(temp_key, temp_value)

    #                 next_index = (next_index + 1) % (self.size - 1)
                
    #             load = self.pairs / self.size
    #             if load < self.minLoad:
    #                 self.resize()
                
    #             return
    #         index = (index + 1) & (self.size - 1)



