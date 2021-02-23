'''
Given two lists a and b. Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value. Your task is to find an element from a and an element form b such that the sum of their values is less or equal to target and as close to target as possible. Return a list of ids of selected elements. If no pair is possible, return an empty list.

Input
a, a list of integer pairs where the first integer represents the unique id and the second integer represents a value.

b, a list of integer pairs where the first integer represents the unique id and the second integer represents a value.

target, an integer representing the target number.

Examples
Example 1:
Input:
a = [[1, 2], [2, 4], [3, 6]], b = [[1, 2]], target = 7,

Output: [[2, 1]]
Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.

Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.

Example 2:
Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]], b = [[1, 2], [2, 3], [3, 4], [4, 5]], target = 10,

Output: [[2, 4], [3, 2]]
Explanation:
There are two pairs possible. Element with id = 2 from the list a has a value 5, and element with id = 4 from the list b also has a value 5.

Combined, they add up to 10. Similarly, element with id = 3 from a has a value 7, and element with id = 2 from b has a value 3.

These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].

Example 3:
Input:
a = [[1, 8], [2, 7], [3, 14]], b = [[1, 5], [2, 10], [3, 14]], target = 20,

Output: [[3, 1]]
Example 4:
Input:
a = [[1, 8], [2, 15], [3, 9]], b = [[1, 8], [2, 11], [3, 12]], target = 20,

Output: [[1, 3], [3, 2]]
'''

from typing import List

class Solution():
    def optimalUtilization(self, listA: List[int], listB: List[int], target: int) -> List[tuple]:
        # First we are going to sort both lists
        # Then we are going to try listA[i], listB[q], and move the values closer to the center.
        # If we ever have a pair that is equal, return
        listA.sort(key = lambda t: t[1])
        listB.sort(key = lambda t: t[1])

        i, q = 0, len(listB) - 1
        bestSum, bestPair = float('inf'), []

        while i < len(listA) and q >= 0:
            # Trying pairs
            listAValue = listA[i]
            listBValue = listB[q]

            pairSum = listAValue[1] + listBValue[1]
            pair = [listAValue[0], listBValue[0]]
            pairDistance = (target - pairSum)

            if pairDistance == bestSum:
                bestPair.append(pair)
                q -= 1

            elif pairDistance < bestSum and pairDistance >= 0:
                bestPair = []
                bestPair.append(pair)
                bestSum = pairDistance
                i += 1

            else:
                # Either our pair isn't good or we are greater than target
                if pairSum > target:
                    # This pair is too big. Decrementing our q if we can
                    q -= 1
                    if q < 0:
                        break

                else:
                    # This pair just isn't good enough. Moving positively
                    i += 1
                    if i >= len(listA):
                        break

        return [bestPair]


s = Solution()
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
t = 10
print(s.optimalUtilization(a,b,t))
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
t = 7
print(s.optimalUtilization(a,b,t))
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
t = 20
print(s.optimalUtilization(a,b,t))
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
t = 20
print(s.optimalUtilization(a,b,t))