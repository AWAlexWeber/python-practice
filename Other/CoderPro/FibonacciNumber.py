''' Calculate the Nth fibonacci number. '''

class Solution:
    def fibonacci(self, k: int, h: dict={0: 0, 1: 1, 2: 1}) -> int:
        if k < 0:
            return 0
        if k not in h:
            h[k] = self.fibonacci(k - 1, h) + self.fibonacci(k - 2, h)
        return h[k]

s = Solution()
print(s.fibonacci(6))
