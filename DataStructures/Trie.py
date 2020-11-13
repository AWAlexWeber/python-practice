# Trie data structure
class TrieNode:
    
    def __init__(self, v: str):
        # This characters value
        self.v = v
        
        # All of the next possible characters, as a hash map
        self.nextCharacters = {}
        self.terminal = False
        
    def contains(self, v: str):
        return v in self.nextCharacters
        
    def get(self, v: str):
        return (self.nextCharacters[v] if v in self.nextCharacters else None)
    
    def add(self, v: str, node):
        self.nextCharacters[v] = node


class Trie:

    def __init__(self):
        # Creating our header
        self.head = TrieNode("")
        

    def insert(self, word: str) -> None:        
        # Getting current head
        currentNode = self.head
        for c in word:
            if currentNode.contains(c):
                currentNode = currentNode.get(c)
            else:
                newNode = TrieNode(c)
                currentNode.add(c, newNode)
                currentNode = newNode
        
        currentNode.terminal = True
        

    def search(self, word: str) -> bool:
        # Searching for our target word
        currentNode = self.head
        
        for c in word:
            if currentNode.contains(c):
                currentNode = currentNode.get(c)
            else:
                return False
            
        return currentNode.terminal

        
    def startsWith(self, prefix: str) -> bool:
        # Checking for initial prefixes
        currentNode = self.head
        
        for c in prefix:
            if currentNode.contains(c):
                currentNode = currentNode.get(c)
            else:
                return False
            
        return True