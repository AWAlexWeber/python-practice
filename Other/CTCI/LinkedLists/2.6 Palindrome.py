from LinkedList import *

def isPalindrome(l: LinkedList) -> bool:
    # Getting the linked list as a string then comparing
    # This is O(n) * 2 more or less
    s = [0] * 100
    i = 0    
    n = l.head

    while n:
        s[i] = n.val
        n = n.node
        i += 1

    totalLen = i / 2
    i -= 1
    c = 0
    while i > totalLen:
        if s[c] != s[i]:
            return False
        c+= 1
        i-=1
    return True

# Generating our test case
testCase = randomLinkedList(15)
testCasePalindrome = LinkedList()

for n in range(1,10):
    testCasePalindrome.addAtHead(n)

for n in range(10, 0, -1):
    testCasePalindrome.addAtHead(n)

print(isPalindrome(testCase))
print(isPalindrome(testCasePalindrome))