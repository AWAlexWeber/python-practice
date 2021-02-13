# Implement an algorithm to determine if a string has all unique characters

# Using a set to map whether or not we have a previous value
def isUniqueHash(s: str):
    h = set()
    for c in s:
        if c in h:
            return False
        else:
            h.add(c)
    return True

# Implement an algorithm to determine if a string has all unique characters without using an additional datastructure
# Sorting it beforehand then just comparing each character with the next. Any match means invalid
def isUniqueSorted(s: str):
    s = sorted(s)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True

# Using a bit vector, a 1d array of size N where N is the size of the alphabet
# In this case, we are going to use a full 90ish sized ascii table via http://www.asciitable.com
# This approach uses a good chunk of memory but does not use any other datastructures
def isUniqueBitVector(s: str):
    v = [0] * 94
    for c in s:
        if v[ord(c) - 94]:
            return False
        else:
            v[ord(c) - 94] = 1
    return True

# Test cases 
testCases = ["abcdefg","aabbccddeeffgg","abel","","aaaaaaaaaaaaaaaaaaa", "gfedcba", "gfdacdefga"]
for t in testCases:
    print(str(isUniqueHash(t))+"\t"+str(isUniqueSorted(t))+"\t"+str(isUniqueBitVector(t)))