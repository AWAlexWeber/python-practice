'''
Given a string representing a roman numeral return the value in decimal
'''

class Solution:
    def romanNumeralToDecimal(self, roman: str) -> int:
        romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        idx, output = 0, 0

        while idx < len(roman):
            c = roman[idx]
            if idx < len(roman) - 1 and romanMap[c] < romanMap[roman[idx + 1]]:
                output += romanMap[roman[idx + 1]] - romanMap[c]
                idx += 2
            else:
                output += romanMap[c]
                idx += 1

        return output

s = Solution()
print(s.romanNumeralToDecimal('MCMIV'))
print(s.romanNumeralToDecimal('IX'))
print(s.romanNumeralToDecimal('VII'))
print(s.romanNumeralToDecimal('MMMMMMMMDCCCLXXXVIII'))