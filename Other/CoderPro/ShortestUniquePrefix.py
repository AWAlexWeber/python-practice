'''
Given a list of strings, return the shortest unique prefix within that string.
jon, john, jack, techlead -> jon, joh, ja, t
'''

from typing import List

class Trie:
    def __init__(self, value: str):
        self.children = {}
        self.isTerminal = False
        self.value = value
        self.count = 0

class Solution:
    def shortestUniquePrefix(self, words: List[str]) -> List[str]:
        # Building our trie
        rootTrie = Trie('')
        for word in words:
            trie = rootTrie
            for c in word:
                if c not in trie.children:
                    trie.children[c] = Trie(c)
                trie = trie.children[c]
                trie.count += 1
            trie.isTerminal = True

        # Going through all of the nodes within the trie, and upon encountering a count of 1 we return
        output = list()
        for word in words:
            currentString = list(word[0])
            trie = rootTrie.children[word[0]]
            idx = 1
            while trie.count > 1:
                c = word[idx]
                trie = trie.children[c]
                currentString.append(c)
                idx += 1

            output.append(''.join(currentString))
        return output

s = Solution()
print(s.shortestUniquePrefix(['jon','john','jack','techlead']))