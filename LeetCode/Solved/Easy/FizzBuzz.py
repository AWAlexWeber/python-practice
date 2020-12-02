''' Famous fizz buzz '''

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        o = list()
        for i in range(1,n + 1):
            s = ''
            if i % 3 == 0:
                s += 'Fizz'
            if i % 5 == 0:
                s += 'Buzz'
            elif i % 3 != 0 and i % 5 != 0:
                s += str(i)
            o.append(s)
        return o