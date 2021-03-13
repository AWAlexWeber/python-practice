'''
Phone numbers. Given a dictionary of all possible strings and a phone number, determine what strings can be made from those phone numbers.
'''

from typing import List

class Solution:
    def phoneNumberDictionary(self, phoneNumber: str, wordDictionary: List[str]) -> List[str]:
        # Building our map from values to characters
        phoneNumberMap = {
            '2': 'ABC',
            '3': 'DEF',
            '4': 'GHI',
            '5': 'JKL',
            '6': 'MNO',
            '7': 'PQRS',
            '8': 'TUV',
            '9': 'WXYZ'
        }

        words = set(wordDictionary)
        output = list()

        # Basic DFS search
        def dfs(phoneNumber: str, currentString: str):
            if len(phoneNumber) <= 0:
                if currentString.lower() in words:
                    output.append(currentString)
                return

            currentNumber = phoneNumber[0]
            for character in phoneNumberMap[currentNumber]:
                nextString = currentString + character
                nextNumber = phoneNumber[1:]
                dfs(nextNumber, nextString)

        dfs(phoneNumber, '')
        return output

s = Solution()
print(s.phoneNumberDictionary('364',['dog','cat','fat','fog']))