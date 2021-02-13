from LinkedList import *

# Return the Kth to last element in a linked list
# ie if we have 5 -> 2 -> 9 -> 3 -> 4 the 2nd from last is 9

# This just prints the value
# TODO: Implement this properly
def returnKthToLast(l: Node, t: int) -> int:
    if l == None:
        return 1

    v = returnKthToLast(l.node, t)

    if v == t:
        print(l.val)
        return v + 1

    else:
        return v + 1

testCase = randomLinkedList(50)
testCase.print()
returnKthToLast(testCase.head, 5)