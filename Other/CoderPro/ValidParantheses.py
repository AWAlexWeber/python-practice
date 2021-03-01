'''
Valid Parantheses

Given a string composed of {} () [] determine if the parantheses are valid
'''
class Solution(object):
  def isValid(self, s):

    parens = {
      '[' : ']',
      '{' : '}',
      '(' : ')',
    }
    inv_parens = {v:k for k,v in parens.items()}

    stack = []
    for c in s:
      if c in parens:
        stack.append(c)
      elif c in inv_parens:
        if len(stack) == 0 or stack[-1] != inv_parens[c]:
          return False
        else:
          stack.pop()
    return len(stack) == 0

print(Solution().isValid('(){([])}'))
# True

print(Solution().isValid('(){(['))