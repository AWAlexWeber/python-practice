# Circular array
# Circular array combines some of the benefits of a normal array with random access and the abilities of a double linked list
# Circular array is one way of implementing a FIFO queue while enabling random access
import itertools

class CircularArray:

    

    def __init__(self, maxSize=10, growthFactor=2):
        # Left tracks the 'left most' position, right tracks the 'right most' position
        # Left will be the output of the queue (the first-most element) and right will be the most recently inserted
        self.data, self.maxSize, self.size, self.left, self.right = [0] * maxSize, maxSize, 0, 0, 0

        # Growth factor
        self.growthFactor = growthFactor

    def getValue(self, index):
        # Get the value at a specific index

        if index >= self.size:
            return None

        index += self.left
        if index >= self.maxSize:
            index = 0 + (index - self.maxSize)
        return self.data[index]

    def append(self, node):
        # Given a data value, append it into our array and move one index to the right
        # If we hit our maximum size, we will grow
        self.data[self.right] = node

        self.right, self.size = self.right + 1, self.size + 1
        
        # Wrap our right value
        if self.right >= self.maxSize:
            self.right = 0

        # If we have reached our size limits, grow
        if self.size >= self.maxSize - 1:
            self.grow()

    def pop(self):
        # If we have data left, pop out the data at the front of the queue, and shrink the queue
        if self.size == 0:
            return None
        
        else:
            node = self.data[self.left]
            self.left = self.left + 1

            if self.left >= self.maxSize:
                self.left = 0

            self.size -= 1

            return node

    def grow(self):
        # Growing our array size
        # This is essentially duplicating
        newSize = self.maxSize * self.growthFactor
        newData = [0] * newSize
        i = 0

        for n in self:
            newData[i] = n
            i = i + 1

        self.maxSize = newSize
        self.data = newData
        self.left = 0
        self.right = i

    def __iter__(self):
        # If our right side is greater than our left side we can simply return an interator
        if self.left <= self.right:
            return iter(self.data[self.left:self.right])
        else:
            # Left is greater than right, meaning we need to combine the two
            return itertools.chain(self.data[self.left:self.maxSize], self.data[0:self.right])

    def __str__(self):
        o, i = [''] * self.size, 0
        for n in self:
            o[i], i = str(n) + " ", i + 1
        return ''.join(o)

c = CircularArray()
for i in range(0,10):
    c.append(i)
for i in range(0,5):
    c.pop()
print(c)
print(c.getValue(0))