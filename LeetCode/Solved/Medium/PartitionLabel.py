'''
763. Partition Labels

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
'''


from typing import List

# Not necessarily the fastest solution, but O(n) with bad constant
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        h, o, j, s = {}, [], 0, -1
        for i, c in enumerate(S):
            h[c] = i

        while j < len(S):
            m = h[S[j]]
            
            while j < m:
                c = S[j]
                m = max(h[c],m)
                j += 1
                
            o.append(m - s)
            s = j
            j += 1
            
        return o
                
        