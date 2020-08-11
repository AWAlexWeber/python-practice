'''
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# Slow solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Representations of our left and right most index
        l, r = (0,0)
        max = 0

        # Dictionary of every 'mapped' value that we have visisted
        m = {}

        # Expanding our window size for every increment that we do not have a match
        while r < len(s):

            if m.__contains__(s[r]):
                if r - l > max:
                    max = r - l

                # Jumping to previous position
                l = m[s[r]] + 1
                r = l

                m = {}

            m[s[r]] = r
            r+=1

        if r - l > max:
            max = r - l

        return max

    # Optimized solution that uses a sliding window approach
    def lengthOfLongestSubstringSlidingWindow(self, s: str) -> int:
        n = len(s)
        oset = set()

        # Iterating 
        a = i = j = 0
        while i < n and j < n:
            # Attempting to extend our window
            if s[j] not in oset:
                oset.add(s[j])
                j+= 1
                a = max(a, j - i)
            else:
                oset.remove(s[i])
                i += 1
        
        return a