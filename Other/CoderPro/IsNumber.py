'''
Check if a string is a number.

123 is a number
12.3 is a number
-123 is a number
+123 is a number
1.5e5 is a number
-.3 is a number

-123-2 is not a number
12a is not a number
111e is not a number
'''

class Solution:
    def isNumber(self, number: str) -> bool:
        containsDecimal, containsExponent = False, False
        for idx, c in enumerate(number):
            if c == '.':
                if containsDecimal:
                    return False
                elif idx == len(number) - 1:
                    return False
                else:
                    containsDecimal = True
            elif c == 'e':
                if containsExponent:
                    return False
                elif idx == len(number) - 1:
                    return False
                else:
                    containsDecimal = False
                    containsExponent = True
            elif c == '-' or c == '+':
                if idx > 0 and number[idx - 1] == 'e':
                    continue
                if idx != 0:
                    return False
            elif c.isnumeric():
                continue
            else:
                return False
        return True
                
s = Solution()
print(s.isNumber("123"))
print(s.isNumber("12.3"))
print(s.isNumber("-123"))
print(s.isNumber("+123"))
print(s.isNumber("1.5e5"))
print(s.isNumber("1.5e1.5"))
print(s.isNumber("25.525e.5"))
print(s.isNumber("-.3e-.3"))

print(s.isNumber("-123-2"))
print(s.isNumber("12a"))
print(s.isNumber("25.525e.-5"))
print(s.isNumber("3e-."))