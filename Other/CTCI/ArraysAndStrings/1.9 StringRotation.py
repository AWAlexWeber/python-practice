# Check if one string is a rotation of another string
# Where s is the main string and p is the possible rotation

# This is a very python-esque solution
def isStringRotation(s: str, p: str) -> bool:
    return (p+p).__contains__(s)

# Test cases
testCases=[["abcdefghijklmnopqrstuvwxyz","bcdefghijklmnopqrstuvwxyza"], ["waterbottle","erbottlewat"], ["aabbc","abcdef"]]
for t in testCases:
    print(isStringRotation(t[0],t[1]))