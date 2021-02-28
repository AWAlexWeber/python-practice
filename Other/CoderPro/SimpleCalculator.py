'''
Given a string representing a mathematical expression:

-(3+(2-1)) = -4
1+1
-1+-1
'''

# Approach could be to solve recursively and apply any modifiers on top.
# We will of course assume properly formatted input values because why not

class Solution:
    def simpleCalculator(self, calc: str) -> int:
        return self.processCalc(calc, 0, len(calc))

    def processCalc(self, calc: str, i: int, j: int) -> int:
        # Recursive function
        # First we have to see if we lead with a negative
        isNegative = (calc[i] == '-')

        # Now we need to find the left and right side.
        # Note that if we hit a parenthesis before a number, we send everything inside of the parenthesis into another process calc
        if isNegative:
            i += 1

        # Alright now starting from the left we look to see if we run into a number or a parenthesis

        for c in range(i, j):
            if calc[i].isnumeric():
                # We found a number first.
                # Now we are goign to find the next operator.
                lMax = -1
                for f in range(c, j):
                    if not calc[f].isnumeric():
                        lMax = f
                        break

                if lMax == -1:
                    return int(calc[c:j])

                # We have found the total range of our left side.
                # It is from c to lMax and it is a number.
                # Now we assume that everything else to be calculated lies between lMax and j
                operator = calc[lMax]
                rVal = self.processCalc(calc, lMax + 1, j)

                # Performing our operation
                lVal = int(calc[c:lMax])

                if isNegative:
                    lVal *= -1

                return self.performCalc(lVal, rVal, operator)

            elif calc[i] == '(':
                # We must find the opposite end parentheses
                for f in range(j - 1, i - 1, -1):
                    if calc[f] == ')':
                        mainVal = self.processCalc(calc, i + 1, f)
                        if isNegative:
                            mainVal *= -1
                        return mainVal

    def performCalc(self, lVal: int, rVal: int, operator: str):
        if operator == '+':
            return lVal + rVal
        if operator == '-':
            return lVal - rVal
            

s = Solution()
print(s.simpleCalculator('(1+(2+(3+(4+105))))'))
print(s.simpleCalculator('12345'))
print(s.simpleCalculator('1+1'))
print(s.simpleCalculator('2-(2+3)'))
print(s.simpleCalculator("2-1+2"))
print(s.simpleCalculator('(1+(4+5+2)-3)+(6+8)'))
            