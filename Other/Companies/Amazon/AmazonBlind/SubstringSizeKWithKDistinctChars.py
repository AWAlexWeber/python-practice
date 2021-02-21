'''
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Examples
Example 1:
Input: s = awaglknagawunagwkwagl,k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation:
Substrings in order are: wagl, aglk, glkn, lkna, kna", gawu, awun, wuna, unag, nagw, agwk, kwag, wagl wagl is repeated twice, but is included in the output once.

Example 2:
Input: s = abcabc,k = 3
Output: ["abc", "bca", "cab"]
Example 3:
Input: abacab = abcabc,k = 3
Output: ["bac", "cab"]
Constraints:
The input string consists of only lowercase English letters [a-z] 0 ≤ k ≤ 26
'''

from typing import List
from collections import defaultdict

# This is essentially a 'largest substring with unique characters' problem, except our sliding window size is fixed
class Solution():
    def substringList(self, k: int, s: str) -> List[str]:
        if len(s) < k:
            return []
            
        # Keeping track of what character's we've visisted. Anytime we get a non unique value we through it into our set.
        nonUnique = set()
        letterCount = defaultdict(lambda: 0)
        output = list()
        outputVisit = set()

        i = 0
        while i < k:
            c = s[i]
            letterCount[c] += 1
            if letterCount[c] > 1 and c not in nonUnique:
                nonUnique.add(c)
            i += 1

        print(nonUnique,letterCount)

        if len(nonUnique) <= 0:
            st = s[i - k + 1:i + 1]
            if st not in outputVisit:
                output.append()
                outputVisit.add(st)
            
        while i < len(s):
            c = s[i]
            rc = s[i-k]

            letterCount[c] += 1
            if letterCount[c] > 1 and c not in nonUnique:
                nonUnique.add(c)

            letterCount[rc] -= 1
            if letterCount[rc] == 1 and rc in nonUnique:
                nonUnique.remove(rc)

            if letterCount[rc] <= 0:
                del letterCount[rc]

            if len(nonUnique) <= 0:
                st = s[i - k + 1:i + 1]
                if st not in outputVisit:
                    output.append(st)
                    outputVisit.add(st)

            i += 1

        return output

s = Solution()
print(s.substringList(4,"awaglknagawunagwkwagl"))

            
