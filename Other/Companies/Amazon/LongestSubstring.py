'''
Longest substring without repeating characters

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

from typing import List

class Solution:

    # One pass solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = k = 0
        o, n = set(), len(s)

        while i < n and j < n:
            if s[j] not in o:
                o.add(s[j])
                j += 1
                k = max(k, j - i)
            else:
                o.remove(s[i])
                i += 1
        return k

    # Similar solution but more wordy
    def lengthOfLongestSubstringLonger(self, s: str) -> int:
        if len(s) <= 0:
            return 0

        # Iterators
        i, j, t, h, b = 0, 0, 1, {s[0]: 1}, set()

        # Iterating until our window hits the end
        while j < len(s) - 1:
            j += 1
            c = s[j]

            # Inserting our value into the dictionary
            if c in h:
                h[c] = h[c] + 1
            else:
                h[c] = 1

            # Checking if we have a valid value
            if (h[c] == 1) and len(b) == 0:
                t += 1

            else:
                # Popping whatever is at i and incrementing i
                a = s[i]
                
                h[a] = h[a] - 1

                # Checking if we just popped a bad duplicate
                if h[a] <= 1 and a in b:
                    b.remove(a)

                # Checking if what we arrived to is now a bad duplicate
                if h[c] > 1 and c not in b:
                    b.add(c)

                # Incrementing i
                i += 1

        return t

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))