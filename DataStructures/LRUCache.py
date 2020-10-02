class LRUNode:
    def __init__(self, key, value, next=None, prev=None):
        self.key, self.value, self.next, self.prev = key, value, next, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        # Top of the cache
        self.head = None
        self.bottom = None

        self.data = {}
        
    def get(self, key: int) -> int:
        if key in self.data:
            self.update(key, self.data[key].value)
            return self.data[key].value
        else:
            return -1       

    def put(self, key: int, value: int) -> None:
        self.update(key, value)

        if self.size > self.capacity:
            self.pop()

    def update(self, key: int, value: int) -> None:
        if self.head == None:
            n = LRUNode(key, value)
            self.head = n
            self.bottom = n
            self.data[key] = n
            self.size += 1
        else:
            # Head exists
            if key in self.data:
                # This node already exists
                # Therefor, we need to move it around
                node = self.data[key]

                if node == self.head:
                    return
        
                prev, next = node.prev, node.next

                # Assigning next/prev allowing us to sneak this node out
                if prev != None:
                    prev.next = next
                if next != None:
                    next.prev = prev

                # Is this value the current bottom?
                if self.bottom == node and self.size > 1:
                    self.bottom = node.next

                # Moving it to the front of the queue
                self.head.next = node
                node.prev = self.head
                node.next = None
                self.head = node

            else:
                # This value does not already exist
                # Creating a new one
                # Note that this does increase the size
                self.size += 1

                node = LRUNode(key, value)

                self.data[key] = node

                # Moving it to the head
                self.head.next = node
                node.prev = self.head
                self.head = node

                if self.size == 2:
                    self.bottom = self.head.prev

    def pop(self) -> None:
        # Removing the value at the bottom of our linked list
        key = self.bottom.key
        self.bottom = self.bottom.next
        self.bottom.prev = None

        # Deleting the key entry
        del self.data[key]

    def print(self):
        n = self.bottom
        while n != None:
            print("("+str(n.key)+","+str(n.value)+")",end=", ")
            n = n.next
        print("")