# Given two strings, write a method to decide if one is a permutation of the other

# First approach will involve a bit vector where we subtract when a value is found in one, and add when one is found in another
# This has additional space complexity constant (though constant space complexity) of O(94)
# However the time complexity is O(n + m) where n and m are the two strings
def checkPermutationBitVector(a: str, b: str) -> bool:
    v = [0] * 94
    
    for c in a:
        v[ord(c) - 94] += 1
    for c in b:
        v[ord(c) - 94] -= 1
    for b in v:
        if b != 0:
            return False
    return True

    ''' 
    There is a slight improvement we can make to this last bit here...
    v = [0] * 94
    
    for c in a:
        v[ord(c) - 94] += 1
    for c in b:
        v[ord(c) - 94] -= 1
    for b in v:
        if b != 0:
            return False
    return True

    We iterate a second time through the bit vector, but we know that this iteration will only reduce it, so we can just check if we are below 0

    We can also increase it slightly by checking for invalid string lengths at the start

    The solution below accomplishes that
    '''

def checkPermutationBitVectorFaster(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False

    v = [0] * 94
    
    for c in a:
        v[ord(c) - 94] += 1
    for c in b:
        v[ord(c) - 94] -= 1
        if v[ord(c) - 94] < 0:
            return False
    return True
        

# Sorting the strings first. This reduces our extra space complexity but will increase our time complexity to O(log(n) + log(m))
def checkPermutationSorted(a: str, b: str) -> bool:
    # Using pythons comparison here to make this faster
    # This is essentailly iterating over each character 
    return sorted(a) == sorted(b)

    '''
    Note that the sorted solution can run faster if you use a radix/counting sort of some type
    Each sort then becomes O(n + k) + O(m + l) where (n,k) (m,l) are the number of characters and character bit size for both strings, respectively
    '''

# Test cases
testCases = [["fat cat", "aat ctf"],["hellothereiamgood","iamgoodtherehello"],["abcdefg","hijklmnop"]]

for t in testCases:
    print(str(checkPermutationBitVector(t[0],t[1]))+"\t"+str(checkPermutationBitVectorFaster(t[0],t[1]))+"\t"+str(checkPermutationSorted(t[0],t[1])))