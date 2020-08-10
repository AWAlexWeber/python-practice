### This question is very easy
class Solution:
    def generateTheString(self, n: int) -> str:
        o = ['a'] * n
        if n % 2 == 0 and n > 0:
            o[0] = 'b'
        return ''.join(o)