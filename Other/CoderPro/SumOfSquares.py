'''
Find the minimal number of values that, when squared, equal a target value.
'''

class Solution:
    def numSquares(self, k: int) -> int:
        count = 0
        while k != 0:
            k -= self.getNextHighestSquare(k)**2
            count += 1
        return count

    def getNextHighestSquare(self, k: int) -> int:
        # Going to use binary search to find the next largest square value
        if k == 1:
            return 1

        left, right = 0, k
        while left <= right:
            mid = (left + right) // 2
            if mid**2 <= k and (mid+1)**2 > k:
                return mid
            else:
                if mid**2 > k:
                    right = mid - 1
                else:
                    left = mid + 1
        return mid

s = Solution()
print(s.numSquares(260))