'''
Create a stack that operates as a stack while also containing a max function.
'''

class MaxStack:
    def __init__(self):
        self.size = 0
        self.data = list()

        self.currentMax = float('-inf')
        self.maxStack = list()

    def push(self, data: int):
        self.data.append(data)
        self.size += 1

        self.currentMax = max(data, self.currentMax)
        self.maxStack.append(self.currentMax)

    def pop(self) -> int:
        if self.size > 0:
            output = self.data.pop()
            self.size -= 1
            self.maxStack.pop()
            return output
        else:
            return None

    def getMax(self) -> int:
        return self.maxStack[-1]

m = MaxStack()
for i in [1,5,2,6,8,9,3,1,34,56,2,21,6,7,8,9,1]:
    m.push(i)
    print(m.getMax(),end=" ")
