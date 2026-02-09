class DynamicArray:
    def __init__(self):
        self.cap = 1
        self.len = 0
        self.arr = [None] * self.cap

    def __len__(self):
        return self.len
    
    def is_empty(self):  # ✅ No double underscores
        return self.len == 0
    
    def __str__(self):
        res = [str(self.arr[i]) for i in range(self.len)]
        return f"[{', '.join(res)}] (length={self.len}, capacity={self.cap})"
    
    def get(self, i: int):
        if i < 0 or i >= self.len:  
            raise IndexError(f"Index {i} out of range [0, {self.len})")
        return self.arr[i]
    
    def set(self, i: int, val):
        if i < 0 or i >= self.len:  
            raise IndexError(f"Index {i} out of range [0, {self.len})")
        self.arr[i] = val

    def _resize(self, new_capacity):  
        new_arr = [None] * new_capacity
        for i in range(self.len):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.cap = new_capacity

    def append(self, val):
        if self.len == self.cap:
            self._resize(self.cap * 2) 
        self.arr[self.len] = val
        self.len += 1

    
    
    
        






if __name__ == "__main__":
    print([None] * 10)