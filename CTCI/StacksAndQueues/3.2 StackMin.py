# Design a stack which in addition to push and pop, tracks the minimal value
# Note that this is O(n) extra space compared to a normal stack (but with O(1) time complexity)
class MinStack():

    def __init__(self, buffer: int):
        self.data = [0] * buffer

        # This helps us track the minimal value that each node has prior to it
        self.minData = [0] * buffer
        self.size = 0

    def add(self, v):
        self.data[self.size] = v
        self.setMin(v)
        self.size += 1

    def pop(self):
        self.size -= 1
        v = self.data[self.size]
        self.minData[self.size] = 0
        self.data[self.size] = 0
        return v

    def getMin(self):
        return self.minData[self.size - 1]
    
    def setMin(self, v):
        # Setting the minimal value
        if self.size == 0 or v < self.minData[self.size - 1]:
            self.minData[self.size] = v
        else:
            self.minData[self.size] = self.minData[self.size - 1]

# This is a more complex solution that actually accomplishes the min in O(1) extra space by using a value comparison
# Effectively whenever we push, we push 2x - minElem into the stack instead of x so that we can retrive the previous minimal element using the current min element
# Taken from geeks for geeks

# Class to make a Node  
class Node: 
    # Constructor which assign argument to nade's value  
    def __init__(self, value): 
        self.value = value 
        self.next = None
  
    # This method returns the string representation of the object. 
    def __str__(self): 
        return "Node({})".format(self.value) 
      
    # __repr__ is same as __str__ 
    __repr__ = __str__ 
  
  
class Stack: 
    # Stack Constructor initialise top of stack and counter. 
    def __init__(self): 
        self.top = None
        self.count = 0
        self.minimum = None
          
    # This method returns the string representation of the object (stack). 
    def __str__(self): 
        temp = self.top 
        out = [] 
        while temp: 
            out.append(str(temp.value)) 
            temp = temp.next
        out = '\n'.join(out) 
        return ('Top {} \n\nStack :\n{}'.format(self.top,out)) 
          
    # __repr__ is same as __str__ 
    __repr__=__str__ 
      
    # This method is used to get minimum element of stack 
    def getMin(self): 
        if self.top is None: 
            return "Stack is empty"
        else: 
            print("Minimum Element in the stack is: {}" .format(self.minimum)) 
  
  
  
    # Method to check if Stack is Empty or not 
    def isEmpty(self): 
        # If top equals to None then stack is empty  
        if self.top == None: 
            return True
        else: 
        # If top not equal to None then stack is empty  
            return False
  
    # This method returns length of stack      
    def __len__(self): 
        self.count = 0
        tempNode = self.top 
        while tempNode: 
            tempNode = tempNode.next
            self.count+=1
        return self.count 
  
    # This method returns top of stack      
    def peek(self): 
        if self.top is None: 
            print ("Stack is empty") 
        else:  
            if self.top.value < self.minimum: 
                print("Top Most Element is: {}" .format(self.minimum)) 
            else: 
                print("Top Most Element is: {}" .format(self.top.value)) 
  
    # This method is used to add node to stack 
    def push(self,value): 
        if self.top is None: 
            self.top = Node(value) 
            self.minimum = value 
          
        elif value < self.minimum: 
            temp = (2 * value) - self.minimum 
            new_node = Node(temp) 
            new_node.next = self.top 
            self.top = new_node 
            self.minimum = value 
        else: 
            new_node = Node(value) 
            new_node.next = self.top 
            self.top = new_node 
        print("Number Inserted: {}" .format(value)) 
  
    # This method is used to pop top of stack 
    def pop(self): 
        if self.top is None: 
            print( "Stack is empty") 
        else: 
            removedNode = self.top.value 
            self.top = self.top.next
            if removedNode < self.minimum: 
                print ("Top Most Element Removed :{} " .format(self.minimum)) 
                self.minimum = ( ( 2 * self.minimum ) - removedNode ) 
            else: 
                print ("Top Most Element Removed : {}" .format(removedNode)) 