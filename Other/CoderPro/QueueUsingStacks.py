'''
Implement a queue using only stacks. It should have push and pop which operate as a queue
'''

class Stack:
    def __init__(self):
        self.size = 0
        self.dataList = list()

    def push(self, data: int):
        self.dataList.append(data)

    def pop(self) -> int:
        return self.dataList.pop()

class Queue:
    def __init__(self):
        # Creating our two stacks. One will take data in, the other will return data as it get's popped out.
        self.inputStack = Stack()
        self.outputStack = Stack()

    def push(self, data: int):
        self.inputStack.push(data)

    def pop(self) -> int:
        # First we need to transfer all data from our input stack to our output stack.
        while len(self.inputStack.dataList) > 0:
            self.outputStack.push(self.inputStack.pop())

        # Then we remove a single value from the top of our output stack.
        output = self.outputStack.pop()

        # Then we move all of the data back to the input stack.
        while len(self.outputStack.dataList) > 0:
            self.inputStack.push(self.outputStack.pop())

        return output

q = Queue()
for k in range(5,15):
    q.push(k)