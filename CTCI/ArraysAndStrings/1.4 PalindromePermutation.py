# Given a string, write a function to check if it is a permutation of a palindrome

# Our first solution will simply perform word counting with a bit vector.
# If all the digits are even (for an even length) or all but one of the digits are even (for an odd length) it is a valid palindrome

def permutationPalindrome(s: str) -> bool:
    v = [0] * 94

    for c in s:
        v[ord(c) - 94] += 1

    o, isOdd = 0, len(s) % 2 == 1
    for b in v:
        if b % 2 == 1:
            if o > 0 or not isOdd:
                return False
            elif isOdd:
                o = 1
    return True


# Test cases
testCases=["atcocta","tacocat","amanaplanacanalpanama","aabbcbaa","aaaabbbbc","abcdefg"]
for t in testCases:
    print(permutationPalindrome(t))