'''
A Company has several suppliers for its products. For each of the products, the stock is represented by a list of a number of items for each supplier. As items are purchased, the supplier raises the price by 1 per item purchased. Let's assume Amazon's profit on any single item is the same as the number of items the supplier has left.

For example, if a supplier has 4 items, Amazon's profit on the first item sold is 4, then 3, then 2 and the profit of the last one is 1.

Given a list where each value in the list is the number of the item at a given supplier and also given the number of items to be ordered, write an algorithm to find the highest profit that can be generated for the given product.

Input
The input consists of three arguments:

numSuppliers: an integer representing the number of suppliers

inventory: a list of long integers representing the value of the item at a given supplier

order: a long integer representing the number of items to be ordered.

Output
Return a long integer representing the highest profit that can be generated for the given product.

Constraints
1 <= numSuppliers <= 10^5

1 <= inventory[i] <= 10 ^ 5

0 <= i < numSuppliers

1 <= orders <= sum of inventory

Examples
Example 1:
Input:
numSuppliers = 2

inventory = [3,5]

order = 6

Output: 19
Explanation:
There are two suppliers, one with inventory 3 and the other with inventory 5, and 6 items were ordered The maximum profit is made by selling 1 for 5, 1 for 4, and 2 at 3 and 2 at 2 units profit. The two suppliers are left with a unit of product each. The maximum profit generated is 5 + 4 + 2*3 + 2*2 = 19.
'''


from typing import List

class Solution():
    def findHighestProfit(self, inventory: List[int], order: int) -> int:
        # We are going to first sort the inventory in O(nlogn) time where n is the size of our inventory.
        # Then we are going to iteratively reduce the highest values until our order becomes 0 in O(k) time where k is the number of orders.
        # This could likely be improved (?)
        s = sorted(inventory,reverse=True)
        i, profit = 0, 0
        while order > 0:
            if s[0] > s[i]:
                i = 0
            if i == len(s) - 1 or s[i] >= s[i + 1]:
                profit += s[i]
                s[i] -= 1
                order -= 1
            while i < len(s) - 1 and s[i] < s[i + 1]:
                i += 1
        return profit

s = Solution()
print(s.findHighestProfit([2, 8, 4, 10, 6],20))