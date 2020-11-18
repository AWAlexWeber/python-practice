'''
68. Text Justification

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
'''

from typing import List
import math

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Building default list.
        o = list()
        
        wordIndex = 0
        while wordIndex < len(words):
            # Grabbing as many words as we can before we push them into a list
            wordLength, moveWordIndex = 0, wordIndex
            actualWordLength = 0
            while wordLength < maxWidth and moveWordIndex < len(words):
                # Adding one for the extra space
                actualWordLength += len(words[moveWordIndex])
                wordLength, moveWordIndex = wordLength + len(words[moveWordIndex]) + 1, moveWordIndex + 1
            # Removing one extra space at the end
            wordLength -= 1

            # Did we go over?
            if wordLength > maxWidth:
                moveWordIndex -= 1
                actualWordLength -= len(words[moveWordIndex])
                wordLength -= len(words[moveWordIndex])
                
            isEnd = moveWordIndex == len(words)
            o.append(self.justify(words, actualWordLength, maxWidth, [wordIndex, moveWordIndex], isEnd))
                
            wordIndex = moveWordIndex
            
        return o
        
    # Helper function for justification
    def justify(self, words: List[str], actualWordLength: int, maxWidth: int, numRange: List[int], isEnd: bool) -> str:
        # First we need to calculate the number of extra spaces
        totalNumWords = numRange[1] - numRange[0]
  
        output = ""
        
        if isEnd:
            # Easy left justification with no extra spaces
            for i in range(numRange[0], numRange[1]):
                output += words[i]
                if i != numRange[1] - 1:
                    output += " "
            while len(output) < maxWidth:
                output += " "
        
        elif totalNumWords <= 1:
            # Easy left justification.
            output += words[numRange[0]]
            while len(output) < maxWidth:
                output += " "
                
        else:
            # Okay now we have to do some actual work
            # We have N numbers left, with a total number of extra spaces equal to K
            totalSpaces = maxWidth - actualWordLength
            reduceFlag = (totalSpaces % (totalNumWords - 1)) != 0
            totalSpacesPerWord = math.ceil(totalSpaces / (totalNumWords - 1))
            #print(reduceFlag)
           
            for i in range(numRange[0], numRange[1] - 1):
                output += words[i]
                #print(output,totalSpaces,totalNumWords - 1 - i + numRange[0])
                
                
                if reduceFlag and (totalSpaces % (totalNumWords - 1 - i + numRange[0])) == 0:
                    reduceFlag = False
                    totalSpacesPerWord -= 1
                    
                for x in range(0, totalSpacesPerWord):
                    output += " "
                    totalSpaces -= 1
                    
                
            output += words[numRange[1] - 1]
                
        return output

            
            
        