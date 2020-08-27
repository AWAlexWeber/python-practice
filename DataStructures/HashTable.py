### This implementation is not complete; this is more an exploration of chaining / probing insertion ###

# Hash tables are incredibly strong data structures that provide access, search, insertion, deletion in O(1) (amortized) time
# This is accomplished through the generation of a hash for each incoming data set, and then using that hash for all the above functions
# Note that a bad hashing function can really mess this up, and reduce the time complexity to O(n)

# Best Case
# Access    # Search    # Insertion # Deletion  #
# N/A       #  O(1)     # O(1)      # O(1)      #

# Worst Case
# Access    # Search    # Insertion # Deletion  #
# N/A       #  O(n)     # O(n)      # O(n)      #

# Given an array of size M, our hashing function will, given the input, generate a position from 0-M N
# 0 <= N < M

# N will be calculated the same for all input parameters
# Given a hashing function for a string that simply adds up the decimal values for each character in the string:

# The hash of 'hello' would be
# h = 104
# e = 101
# l = 108
# l = 108
# o = 111
# total = 532
# If our size is 32, we end up with a final position of 532 % 32 = 20, so 'hello' would give us the index of 20
# We could then set that value to another, such as an integer value of 15
# Then accessing the hashtable with an index of 'hello' would yield 15
# Note that the hash of 'loleh' would actually lead to the same index, and this is when we would have to use either chaining or probing

# Chaining / probing are ways of handling hash collisions within a hash table. A good hashing function will make this difficult, but even then it can still happen
# Chaining creates linked lists at the location of the hash; ie in our example of 'hello' and 'loleh', both of which would hash to an index of 20, we create a linked list
# at that index pointing to the values of 'hello' and 'loleh'

# Probing (linear probing in this case) would instead skip to the next index. This would then continue until we had an empty index
# Note that as the hash table becomes more full, probing becomes less and less efficient and chaining becomes better. If you are 99% full, finding that opening index will take a very long time
# known as the load factor. Instead, chaining becomes better (near 90% full)

import random
import string

class HashTableEntry:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:

    def __init__(self, size):
        self.data = [None] * size
        self.size = 0
        self.maxSize = size

    def hash(self, data) -> int:
        # String custom hasing function
        # Real implementations would use something more sophisticated than this
        return hash(data) % self.maxSize

    def add(self, key, value):
        # Calculating the has
        h = self.hash(key)

        # Note that we will only perform linear probing while our max size is at 90%
        if self.size < (self.maxSize * 0.9):
            # Linear probing to the next data value
            while not self.data[h] == None:
                h = (h + 1) % self.maxSize

        # Inserting the value
        e = HashTableEntry(key, value)

        # Inserting into an empty slot
        if not self.data[h]:
            self.data[h] = e
        else:
            # Existing slot, chaining
            n = self.data[h]
            while n.next:
                n = n.next

            n.next = e


        # Incrementing size
        self.size += 1

    def print(self):
        for i in range(0,self.maxSize):
            print(i,end=": ")
            if self.data[i]:
                n = self.data[i]
                while n:
                    print(n.key,n.value,end=" ")
                    n = n.next
                print("")

            else:
                print("EMPTY")

t = HashTable(50)

# Generating our datasets for testing
for i in range(0,100):
    s = [0] * random.randrange(5,25)
    for j in range(0, len(s)):
        s[j] = random.choice(string.ascii_letters)
    
    s = ''.join(s)
    t.add(s,0)

t.print()