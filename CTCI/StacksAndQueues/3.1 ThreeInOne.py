# Implement three stacks using a single array
from typing import List

# This will be accomplished by defining boundaries within this array as the size of each stack
class ArrayStack():
    def __init__(self, data: List[int], minV: int, maxV: int):
        self.data = data
        self.min, self.max = minV, maxV
        self.pos = minV

    # Defining our 
    def add(self, v: int):
        if self.pos == self.max:
            return None

        data[self.pos] = v
        self.pos += 1

    def pop(self):
        if self.pos == self.min:
            return None

        o = data[self.pos]
        data[self.pos] = None
        self.pos -= 1
        return o

# Creating our buffer
buffer = 48
data = [0] * buffer

a1 = ArrayStack(data, 0, buffer//3)
a2 = ArrayStack(data, buffer//3, buffer*2//3)
a3 = ArrayStack(data, buffer*2//3, buffer)