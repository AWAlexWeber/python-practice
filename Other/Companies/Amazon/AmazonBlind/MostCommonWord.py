'''
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words. It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation. Words in the paragraph are not case sensitive. The answer is in lowercase.

Examples
Example 1:
Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." banned = ["hit"]

Output: [ball]
Explanation:
"hit" occurs 3 times, but it is a banned word. "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. Note that words in the paragraph are not case sensitive, that punctuation is ignored (even if adjacent to words, such as "ball,"), and that "hit" isn't the answer even though it occurs more because it is banned.

Note:

1 <= paragraph.length <= 1000.
0 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
There are no hyphens or hyphenated words.
Words only consist of letters, never apostrophes or other punctuation symbols.
'''
from typing import List
from collections import defaultdict
import string

# This is a very straightforward question; we simply count occurences. Time complexity is O(n) and space complexity is O(n) where n is number of words
class Solution():
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Tracking our counts
        counts = defaultdict(lambda: 0)
        maxWord, maxCount = None, 0

        # Building our banned dictionary for O(1) access (assuming proper hasing library)
        bannedDict = set()

        # O(k) time complexity where k is the length of our banned list.
        for word in banned:
            bannedDict.add(word)

        # Making the replacements for puncation. This is O(n) time complexity. Note we are assuming proper sentrance structure by the method caller.
        paragraph = paragraph.translate(str.maketrans('', '', string.punctuation))

        # O(n) where n is the number of characters in our paragraph.
        for word in paragraph.split(' '):
            # O(1)
            if word.lower() not in bannedDict:
                # O(1)
                counts[word.lower()] += 1
                if counts[word.lower()] > maxCount:
                    maxWord, maxCount = word.lower(), counts[word.lower()]

        # Total time: O(n + k) where n is the number of characters and k is the number of banned words. O(n) space complexity, from counting each word.

        return maxWord
            
s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))