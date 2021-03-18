'''
Reverse polish calculator.
1,2,3+2*- is equal to
1 - (2+3) * 2
'''

class Solution:
    def polishCalculator(self, tokens: str) -> int:
        # Using a stack to accomplish this
        s = list()
        for c in tokens:
            if c == '+' or c == '-' or c == '*' or c == '/':
                # Popping the last two elements and performing the operation
                operandTwo = s.pop()
                operandOne = s.pop()
                operatedNumber = None
                
                if c == '+':
                    operatedNumber = (operandOne + operandTwo)
                elif c == '-':
                    operatedNumber = (operandOne - operandTwo)
                elif c == '*':
                    operatedNumber = (operandOne * operandTwo)
                elif c == '/':
                    operatedNumber = int(operandOne / operandTwo)
                s.append(operatedNumber)
                
            else:
                s.append(int(c))

        return s.pop()

s = Solution()
print(s.polishCalculator('123+2*-'))


