'''
771. Jewels and Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''

# All we do is count the number of types a letter in S appears in J
# very self explanatory and straight forward

class Solution:
    # Optimizied solution
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(c in set(J) for c in S)
    
    # My solution
    def oldNumJewelsInStones(self, J: str, S: str) -> int:
        s = set()
        for c in J:
            s.add(c)

        count = 0
        for c in S:
            if s.__contains__(c):
                count += 1

        return count


s = Solution()
print(s.numJewelsInStones("aA", "aAAAAbbb"))