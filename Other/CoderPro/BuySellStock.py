'''
Finding the best time to buy/sell stock given an array of stock prices.
'''

from typing import List

class Solution:
    def buySellStock(self, prices: List[int]) -> int:
        maxSale, maxPrice = float('-inf'), float('-inf')
        for price in prices[::-1]:
            maxPrice = max(maxPrice, price)
            sale = maxPrice - price
            maxSale = max(sale, maxSale)
        return maxSale

s = Solution()
print(s.buySellStock([9, 11, 8, 5, 7, 10]))