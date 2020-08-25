# A skip list is an implementation of a linked list, where we have different layers that skip a certain, variable amount of nodes
# It is an alternative to a b-tree, and while built off of linked list it functions more like a tree

# Best Case
# Access    # Search    # Insertion # Deletion  #
# O(log(n)) # O(log(n)) # O(log(n)) # O(log(n)) #

# Worst Case
# Access    # Search    # Insertion # Deletion  #
# O(n) # O(n) # O(n) # O(n) #

# These worse cases are interesting and largely based off of probability, which we will come back to later
# Note that skiplist has terrible space complexity of O(nlog(n)), the worst of really any major datastructure by a factor of log(n)

# The main idea behind a skip list is that we have multiple linked lists, but some that skip nodes #
# IE

# Given a normal linked list representation of
# 1 2 3 4 5 6 7 8 9
# You would have

# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
# Traversing the length of this linked list is in O(n) time

# Now, in a balanced, binary search tree implementation, we see that we interpret that data as 
#         5
#     3         8
#   2   4     7    9
# 1         6

#  A skip list combines both in a way
# The data for our above set would be represented by

# L4  : -----------------------------------> NIL
# L3  : 1 --------->4 ----->6 -------------> NIL
# L2  : 1 ----->3 ->4 ----->6 --------->9 -> NIL
# L1  : 1 ->2 ->3 ->4 ->5 ->6 ->7 ->8 ->9 -> NIL
# Data: 1   2   3   4   5   6   7   8   9

# Note that if we followed the data along L1, we go through every node in O(n) time
# However, if we utilize L1 through L3 and use binary search, we can get to 9 in O(log(n))
# 6 -> 7 -> 8 -> 9

# Python3 code for inserting element in skip list 
# From https://www.geeksforgeeks.org/skip-list-set-2-insertion/
  
import random 
  
class Node(object): 
    ''' 
    Class to implement node 
    '''
    def __init__(self, key, level): 
        self.key = key 
  
        # list to hold references to node of different level  
        self.forward = [None]*(level+1) 
  
class SkipList(object): 
    ''' 
    Class for Skip list 
    '''
    def __init__(self, max_lvl, P): 
        # Maximum level for this skip list 
        self.MAXLVL = max_lvl 
  
        # P is the fraction of the nodes with level  
        # i references also having level i+1 references 
        self.P = P 
  
        # create header node and initialize key to -1 
        self.header = self.createNode(self.MAXLVL, -1) 
  
        # current level of skip list 
        self.level = 0
      
    # create  new node 
    def createNode(self, lvl, key): 
        n = Node(key, lvl) 
        return n 
      
    # create random level for node 
    def randomLevel(self): 
        lvl = 0
        while random.random()<self.P and lvl<self.MAXLVL:lvl += 1
        return lvl 
  
    # insert given key in skip list 
    def insertElement(self, key): 
        # create update array and initialize it 
        update = [None]*(self.MAXLVL+1) 
        current = self.header 
  
        ''' 
        start from highest level of skip list 
        move the current reference forward while key  
        is greater than key of node next to current 
        Otherwise inserted current in update and  
        move one level down and continue search 
        '''
        for i in range(self.level, -1, -1): 
            while current.forward[i] and current.forward[i].key < key: 
                current = current.forward[i] 
            update[i] = current 
  
        '''  
        reached level 0 and forward reference to  
        right, which is desired position to  
        insert key. 
        ''' 
        current = current.forward[0] 
  
        ''' 
        if current is NULL that means we have reached 
           to end of the level or current's key is not equal 
           to key to insert that means we have to insert 
           node between update[0] and current node 
       '''
        if current == None or current.key != key: 
            # Generate a random level for node 
            rlevel = self.randomLevel() 
  
            ''' 
            If random level is greater than list's current 
            level (node with highest level inserted in  
            list so far), initialize update value with reference 
            to header for further use 
            '''
            if rlevel > self.level: 
                for i in range(self.level+1, rlevel+1): 
                    update[i] = self.header 
                self.level = rlevel 
  
            # create new node with random level generated 
            n = self.createNode(rlevel, key) 
  
            # insert node by rearranging references  
            for i in range(rlevel+1): 
                n.forward[i] = update[i].forward[i] 
                update[i].forward[i] = n 
  
            print("Successfully inserted key {}".format(key)) 
  
    # Display skip list level wise 
    def displayList(self): 
        print("\n*****Skip List******") 
        head = self.header 
        for lvl in range(self.level+1): 
            print("Level {}: ".format(lvl), end=" ") 
            node = head.forward[lvl] 
            while(node != None): 
                print(node.key, end=" ") 
                node = node.forward[lvl] 
            print("") 

# Test code
s = SkipList(3, 0.5)
s.insertElement(3) 
s.insertElement(6) 
s.insertElement(7) 
s.insertElement(9) 
s.insertElement(12) 
s.insertElement(19) 
s.insertElement(17) 
s.insertElement(26) 
s.insertElement(21) 
s.insertElement(25) 
s.displayList() 