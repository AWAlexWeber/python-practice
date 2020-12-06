'''
127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

import heapq 
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Precomputing in O(N^2). This should be improved
        precompute_table = {}
        
        wordList.insert(0, beginWord)
        
        # Checking in O(n) if our end word does not exist. Increase in constant time, should help with edge cases though.
        if endWord not in wordList:
            return 0
        
        for i, word in enumerate(wordList):
            word_match_set = set()
            for match in wordList:
                if word == match:
                    continue
                    
                # Checking to see if the word difference is equal to 1
                if self.wordDistance(word, match):
                    word_match_set.add(match)
                    
            precompute_table[word] = word_match_set
                    
        # We've build our precompute table
        self.m_depth = float('inf')
        
        # Building our heap
        heap = list()
        visit = set()
        
        heapq.heappush(heap, (1, beginWord))
        visit.add(beginWord)
        
        while len(heap) > 0:
            
            # Getting the 'closest' word
            depth, word = heapq.heappop(heap)
            
            if word == endWord:
                return depth
            
            # Inserting the neighbors, adding them to visit
            # Normally this breaks uniform cost search, and we would need to add some functionality for replacement
            # But our directed graph has single cost values, so there should never be a need for replacement.
            
            for neighbor in precompute_table[word]:
                if neighbor in visit:
                    continue
                    
                heapq.heappush(heap, (depth + 1, neighbor))
                visit.add(neighbor)
                
        return 0
                
    def wordDistance(self, word1: str, word2: str) -> bool:
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
            if diff >= 2:
                return False
        return True