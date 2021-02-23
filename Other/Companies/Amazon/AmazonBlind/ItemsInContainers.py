'''
A librarian would like to count the number of enclosed items in row that are between two dividers. A row is represented by a string s, each item is a *, and a divider is represented as |. A list of range tuples are given that represent each substring to consider, and the number of enclosed items for each substring must be returned in a list.

* = ascii number 42
| = ascii number 124
Example 1:
Input: s = |**|*|*, ranges = [[0, 4], [1, 6]]
Output: [2, 3]
Explanation:
The first range to consider is [0, 4] which corresponds to |**|*. There are 2 items in the first enclosed part.

For the second range, [1, 6], the substring is **|*|*, which contain only one enclosed part with one item inside it.

Both of the answers are returned in an array, ie. [2, 1].

Example 2:
Input: s = *|*|, ranges = [[1, 3]]
Output: [1]
Explanation:
The substring from index = 1 to index = 3 is |*|. There is only one item and it is surrounded by two dividers. Therefore, the output is [1].

Constraints:
There are no invalid characters, and each range is non-zero in size and always increasing. The ranges provided are always within the string bounds.
'''

from typing import List

class Solution():
    def itemsInContainers(self, s: str, ranges: List[tuple]) -> List[int]:
        # Brute-force esque solution first. Will revisit with better solution
        output = list()
        # O(nk) where n is the length of s and k is the number of ranges. In an ideal world we would ensure visisted ranges do not get visited again
        for rangeValues in ranges:
            start, end = (rangeValues)
            count, tempCount, seenFirstDivider = 0, 0, False
            for idx in range(start, end + 1):
                ''' Handling entrance into our iteration '''
                if s[idx] == '|' and not seenFirstDivider:
                    seenFirstDivider = True
                    continue

                elif not seenFirstDivider:
                    continue

                ''' Okay we've seen a first divider '''
                if s[idx] == '|':
                    count += tempCount
                    tempCount = 0
                if s[idx] == '*':
                    tempCount += 1

            output.append(count)
        return output

    def itemsInContainersBetter(self, s: str, ranges: List[tuple]) -> List[int]:
        # Better solution in O(n + k) time and O(n) space, where n is the length of s, and k is the number of ranges.
        n = len(s)

        # Creating our prefix sums
        prefix_sums = {}
        cur_sum = 0
        for i in range(n):
            if s[i] == '|':
                prefix_sums[i] = cur_sum
            else:
                cur_sum += 1

        # Building left boundaires
        left_bounds = [-1] * n
        last = -1
        for i in range(n):
            if s[i] == '|':
                last = i
            left_bounds[i] = last

        # Building right boundaries
        right_bounds = [-1] * n
        last = -1
        for i in reversed(range(n)):
            if s[i] == '|':
                last = i
            right_bounds[i] = last

        # Assembling final output values
        res = []
        for start_i, end_i in ranges:
            start = right_bounds[start_i]
            end = left_bounds[end_i]
            if start != -1 and end != -1 and start < end:
                res.append(prefix_sums[end] - prefix_sums[start])
            else:
                res.append(0)
        return res
                
s = Solution()
f = s.itemsInContainersBetter('|**|*|*', [[0,4],[1,6]])
print(f)
f = s.itemsInContainersBetter('*|*|', [[1,3]])
print(f)