'''
Return the total number of binary search trees given a number of nodes.
'''

class Solution:
    def numBinarySearchTrees(self, n: int) -> int:
        # Catalan
        c = 1
        for i in range(0, n):
            c = c * 2*(2*i+1)/(i+2)
            
        return int(c)

s = Solution()
print(s.numBinarySearchTrees(256))