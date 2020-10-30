'''
692. Top K Frequent Words

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
'''


from heapq import heappush, heappop
import collections
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        h = {}
        for w in words:
            if w not in h:
                h[w] = 0
            h[w] += 1
            
        o = list()
        for w in h.keys():
            heappush(o,(-h[w], w))
            
        l = {}
        for i in range(k):
            v = heappop(o)
            w = v[1]
            c = -v[0]
            if c not in l:
                l[c] = list()
            l[c].append(w)
        
        o = list()
        for k in sorted(l.keys())[::-1]:
            for w in sorted(l[k]):
                o.append(w)
                
        return o
        