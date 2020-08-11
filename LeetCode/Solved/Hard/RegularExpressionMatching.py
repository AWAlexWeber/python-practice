'''
10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''

# Definitly considering a recursive approach from the initial look
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# Attempting a brute-force solution
class Solution:
    def isMatchOld(self, s: str, p: str) -> bool:
        # Splitting
        arr = p.split("*")

        # If we have no asterisks, we simply make a string comparison
        if len(arr) <= 1:
            if len(s) != len(p):
                return False
            for i, c in enumerate(s):
                if not self.characterCompare(c, p[i]):
                    return False
            return True

        # Little bit to check if our array ends with an asterisk
        # This helps us later on
        endsInStar = p[len(p) - 1] == "*"

        # Iterating through each variable set
        # Setting our starting index within the total string
        index = 0
        for n, a in enumerate(arr):

            # Enumerating
            for i, c in enumerate(a): 

                # Checking if this is the final array
                hasStar = True
                if n == len(arr) - 1 and not endsInStar:
                    hasStar = False

                if i == len(a) - 1 and hasStar:

                    # Are we a .? If so, we are performing a .* check
                    if c == ".":

                        continueFlag = False

                        # Are we the last true index
                        if n == len(arr) - 2 and endsInStar:
                            return True

                        # We need to find the last index of our next required character in our pattern array
                        for x in range(n + 1, len(arr)):
                            # If our length is greater than 1, grab the first character
                            targetCharacter = ''
                            if len(arr[x]) > 1:
                                targetCharacter = arr[x][0]
                            
                            # If our length is equal to 1, but we are the last element in the array and we don't have an asterisk, then we can also grab our target character
                            if x == len(arr) - 1 and not endsInStar:
                                targetCharacter = arr[x][0]

                            # Did we not find a target character?
                            # That means the rest of our string is a total free for all, all asterisk based positioning
                            # Meaning we know that this is true 
                            if targetCharacter == '':
                                return True

                            # Starting from the end, finding the latest valid index of this
                            newIndex = -1
                            for sci in range(len(s) - 1, index, -1):
                                # As soon as we find that valid index, we move to that position
                                sc = s[sci]

                                if sc == targetCharacter:
                                    newIndex = sci
                                    

                            if newIndex == -1:
                                return False

                            else:
                                index = newIndex
                                continueFlag = True
                                break


                        if continueFlag:
                            continue

                    # We get to move to the right continuously while our character is equal to our target character
                    # Note we can't go too far, so we have a maximum index of the last true index
                    # Checking that edge case here

                    while index < len(s) and self.characterCompare(s[index], c):
                        index += 1

                else:
                    # Iterating over normal values
                    if not self.characterCompare(s[index], c):
                        return False

                    else:
                        index += 1

        # Did we make it to the end?
        if index == len(s):
            return True
        else:
            return False

    # Small helper function that lets us abstract comparing the period value
    def characterCompare(self, c1: str, c2: str):
        #print(c1,c2)
        if c1 == "." or c2 == ".":
            return True
        else:
            return c1 == c2

    def isMatch(self, text, pattern):

        print(text,pattern)

        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            print("first")
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            print("second")
            return first_match and self.isMatch(text[1:], pattern[1:])


s = Solution()
#print(s.isMatch("aa", "a"))
#print(s.isMatch("aa", "a*"))
#print(s.isMatch("ab", ".*"))
#print(s.isMatch("aab", "c*a*b"))
#print(s.isMatch("mississippi", "mis*is*p*."))
print(s.isMatch("aaabbbecafdefdbb", "a*b*.*ef*d*bb"))
#print(s.isMatch("ab",".*c"))
#print(s.isMatch("aaa","a*a"))