'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) <= 0:
            return []

        # Essentially we go one deeper and append on where we currently are
        self.output = []
        self.map = {0: None, 1: None, 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        self.recurseLetter(digits, '')
        return self.output

    def recurseLetter(self, digits: str, previousDigits: str):
        if len(digits) == 0:
            if len(previousDigits) > 0:
                self.output.append(previousDigits)
            return

        d = int(digits[0])

        # Handling 0 and 1
        if not self.map[d]:
            self.recurseLetter(digits[1:], previousDigits)

        for c in self.map[d]:
            self.recurseLetter(digits[1:], previousDigits + c)

s = Solution()
print(s.letterCombinations("23"))