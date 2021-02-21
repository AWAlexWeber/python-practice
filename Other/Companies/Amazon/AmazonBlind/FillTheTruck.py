'''
box.

Given the number of boxes, the truck can hold, write an algorithm to determine the maximum number of units of any mix of products that can be shipped.

Input
The input consists of five arguments:

num: an integer representing the number of products

boxes: a list of integers representing the number of available boxes for products

unitSize: an integer representing size of unitsPerBox

unitsPerBox: a list of integers representing the number of units packed in each box

truckSize: an integer representing the number of boxes the truck can carry.

Output
Return an integer representing the maximum units that can be carried by truck.

Constraints
1 <= |boxes| <= 10^5

|boxes| == |unitsPerBox|

1 <= boxes[i] <= 10^7

1 <= i <= |boxes|

1 <= unitsParBox[i] <= 10^5

1 <= j <= |unitsPerBox|

1 <= truckSize <= 10 ^ 8

Examples
Example 1:
Input:
num = 3

boxes = [1, 2, 3]

unitSize = 3

unitsPerBox = [3, 2, 1]

truckSize = 3s

Output: 7
Explanation:
Product 0: because boxes[0] = 1, we know there is 1 box in product 0. And because unitsPerBox[0] = 3, we know there is 1 box with 3 units in product 0.

Product 1: 2 boxes with 2 units each

Product 2: 3 boxes with 1 unit each

Finally, we have packed products like a list: [3, 2, 2, 1, 1, 1]

The truckSize is 3, so we pick the top 3 from the above list, which is [3, 2, 2], and return the sum 7.

The maximum number of units that can be shipped = 3 + 2 + 2 = 7 units
'''

from typing import List

class Solution():
    def fillTheTruck(self, boxes: List[int], unitsPerBox: List[int], truckSize: int):
        # This is really just a selection algorithm.

        # Really all we're going to do is select the highest scoring unitPerBoxes while truckSize remains above zero.
        numOutput = 0

        # Going to assume that our units per box is not sorted, so going to sort it so its in ascending order.
        # O(nlogn) time complexity. Could make this smaller with radix sort.
        sortedUnits = sorted(zip(boxes,unitsPerBox), key=lambda t: t[1], reverse=True)
        i = 0
        while truckSize > 0:
            while sortedUnits[i][0] == 0:
                i += 1
            selectedBoxes = min(sortedUnits[i][0], truckSize)
            numOutput += selectedBoxes * sortedUnits[i][1]
            truckSize -= selectedBoxes
            sortedUnits[i] = (sortedUnits[i][0] - selectedBoxes, sortedUnits[i][1])
        return numOutput

        # Honestly this complexity is far from perfect, O(nlogn) time (because of sort), O(n) space (because of tracking)
            
            

s = Solution()
print(s.fillTheTruck([1,2,3], [3, 2, 1], 3))

