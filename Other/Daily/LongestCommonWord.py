'''
Given a list of strings, find the longest common word that occurs at least twice.

["Echo", "Alexa", "Kindle", "Echo Show", "Amazon"] -> "Echo"
["Echo Show", "Echo Show 8"] -> "Echo Show"
'''

from typing import List

class Trie:
    def __init__(self, value):
        self.value = value
        self.children = {}

        # Using count to track the number of occurences for this word.
        self.count = 0

class Solution:
    def longestCommonWord(self, words: List[str]) -> str:
        # The idea is that we will insert all words into a trie, and before every space / end of the entire word we check if we have a maximal length such that our values are still greater than 1.
        t = Trie('')
        for word in words:
            # Building our trie
            currentTrie = t
            for c in word:
                if c not in currentTrie.children:
                    currentTrie.children[c] = Trie(c)
                currentTrie.children[c].count += 1
                currentTrie = currentTrie.children[c]

        # Now we simply perform a DFS search.
        o = list()
        def dfs(t: Trie, o: list=list(), w: str='', d: int=0) -> None:
            if len(t.children) == 0 and t.count > 1:
                # We've reached the end of our search. This implies that we've hit the end of a word. Check if this word is bigger.
                if len(o) == 0 or d > len(o[0]):
                    del o[:]
                    o.append(w)
                    return
                elif d == len(o[0]):
                    o.append(w)
                    return

            # Iterating over all children and searching deeper on all children that have a count greater than zero
            for child in t.children.keys():
                if t.children[child].count > 1:
                    newW = w + child
                    dfs(t.children[child], o, newW, d + 1)

            # We've explored all our children, but we will also check if we are the terminating best value.
            if ' ' in t.children and t.count > 1:
                if len(o) == 0 or d > len(o[0]):
                    del o[:]
                    o.append(w)
                elif d == len(o[0]):
                    o.append(w)
        
        # Performing our DFS search.
        dfs(t, o)

        if len(o) != 1:
            return 'None'

        return o[0]

s = Solution()
print(s.longestCommonWord(['Echo','Alexa','Kindle','Echo Show','Amazon']))
print(s.longestCommonWord(["Echo Show", "Echo Show 8"]))
print(s.longestCommonWord(["Eat Show", "Fat Show 8"]))