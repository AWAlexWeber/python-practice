'''
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = list()
        self.dataStack = list()
        self.currentMin = float("inf")
        

    def push(self, x: int) -> None:
        if self.currentMin > x:
            self.currentMin = x
            
        self.dataStack.append(x)
        self.minStack.append(self.currentMin)

    def pop(self) -> None:
        self.dataStack.pop()
        
        # Moving our currentMin to whatever is at the top of the minStack.
        # Unless its emplty, then we set it to inf
        self.minStack.pop()
        
        if len(self.minStack) <= 0:
            self.currentMin = float("inf")
        else:
            self.currentMin = self.minStack[len(self.minStack) - 1]

    def top(self) -> int:
        return self.dataStack[len(self.dataStack) - 1]
        

    def getMin(self) -> int:
        return self.currentMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()