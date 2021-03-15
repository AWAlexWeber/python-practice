''' Given a string and a list of other strings, find all possible completions of the orignial string, giving rankings to the final strings '''

from typing import List
from queue import Queue

class Trie:
    def __init__(self):
        self.children = {}
        self.isTerminal = False
        self.totalRank = 0

class Solution:
    def autocomplete(self, inputStr: str, words: List[tuple], k: int) -> List[str]:
        # First we build a trie using all of the words.
        # O(c) where c is the total number of characters in all of the words.
        root = Trie()
        for wordPair in words:
            currentTrie = root
            word, rank = (wordPair)
            for c in word:
                currentTrie.totalRank += rank
                if c not in currentTrie.children:
                    currentTrie.children[c] = Trie()
                currentTrie = currentTrie.children[c]
            currentTrie.isTerminal = True
                    
        # Attempting to move to our spot in our trie where our input sring is
        # If its not in our trie we return an empty array
        currentTrie = root
        for c in inputStr:
            if c not in currentTrie.children:
                return []
            else:
                currentTrie = currentTrie.children[c]

        # Okay, now what we want to do is explore the remaining trie, finding all terminal values and selecting the highest total rank during search
        output = list()

        q = Queue()
        q.put((currentTrie, inputStr))

        while not q.empty() and len(output) < k:
            currentTrie, currentStr = (q.get())
            if currentTrie.isTerminal:
                output.append(currentStr)

            childrenRanks = [(currentTrie.children[child].totalRank, child) for child in currentTrie.children]
            childrenRanks.sort(reverse=True)
            for (childRank, childValue) in childrenRanks:
                q.put((currentTrie.children[childValue], currentStr + childValue))

        return output

s = Solution()
word = 'hello'
words = [
    ('hello',5),
    ('hell',3),
    ('hello there', 10),
    ('helchi', 1),
    ('helli', 55)
]

print(s.autocomplete(word, words, 3))