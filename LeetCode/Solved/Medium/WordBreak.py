'''
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP using a trie
        root = Trie()
        for word in wordDict:
            root.insertWord(word)
            
        return self.deepen(s, {}, root)
        
    def deepen(self, s: str, visit: dict, trie, start=0) -> bool:
        isDeeper = False
        
        # Wait, are we in our visit path?
        if start in visit:
            return visit[start]
        
        curNode = trie.root
        for i in range(start, len(s)):
            # Attempt to go deeper
            #print(s[i], i, start)
            if s[i] in curNode.children:
                #print("fine, going deeper")
                curNode = curNode.children[s[i]]
                
            # No match means that this is an impossible path
            else:
                #print("exiting")
                visit[start] = isDeeper
                return isDeeper
                
            # Is this terminal
            if curNode.terminal:
                #print("found terminal value")
                # We've found a current break.
                # Is this the end?
                if i == (len(s) - 1):
                    #print("final value, exiting")
                    return True
                
                # Appending a deeper node
                else:
                    #print("deepening at " + str(i + 1))
                    isDeeper = (isDeeper or self.deepen(s, visit, trie, start=(i + 1)))

        #print('finished iteration, returning ' + str(isDeeper))
        return isDeeper
        
class Trie:
    def __init__(self):
        self.root = TrieNode('')
        
    def insertWord(self, word: str):
        # Appending this word
        node = self.root
        for c in word:
            # Traversing until we find the current end of this word
            if c in node.children:
                node = node.children[c]
                continue
                
            # We've found our spot
            tmpNode = TrieNode(c)
            node.children[c] = tmpNode
            node = tmpNode
            
        node.terminal = True
        
class TrieNode:
    def __init__(self, c: chr, terminal=False):
        self.val = c
        self.terminal = terminal
        
        # Mapping a character
        self.children = {}