'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Going to use a hashmap of the mapped integer representation for each word
        # Basically, we can convert any word into a string of integers, where the index of that integer is the character id
        # For example, ABC = 11100000000000000000000000
        
        # Note that anagrams will have the exact same character id.
        # And we get to use constant space and time since we have 26 characters
        
        # Creating default dictionary using a list
        digitMap = defaultdict(lambda: list())

        # O(n) operation where n is the length of our list.
        # Internal operation is O(m) where m is the length of the word.
        # This gives us a total time complexity of O(n*m), which is really O(c) where c is the total number of characters
        for word in strs:
            digitMap[self.convertWordToIntegerString(word)].append(word)
            
        # Nice and simply getting all of the lists. O(n) again.
        output = list()
        for k in digitMap.keys():
            output.append(digitMap[k])
            
        return output
            
    def convertWordToIntegerString(self, word: str) -> str:
        # Converts our word into the digit map
        # This operation is O(m) where m is the length of our word
        cha = [0] * 26
        for c in word:
            cha[ord(c.lower()) - 97] += 1
            
        return str(cha)