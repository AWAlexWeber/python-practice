'''
1282. Group the People Given the Group Size They Belong To

There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 

 

Example 1:

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
 

Constraints:

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n

'''

from typing import List

# This solution takes every element and puts it into a hash that maps the group size to a list of indexes that belong to that list
# This has a high constant but is still O(n)
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Hash set mapping group size to indexes that belong to that group
        h = {}
        
        # O(n) for iterating over 
        for index, val in enumerate(groupSizes):
            # O(1)
            if val not in h:
                h.setdefault(val, [])
                
            # May look dangerous but this is O(1)
            h[val].append(index)
            
        # Iterating over the groups and returning
        out = []
        
        # This is O(k) where K is the number of groups
        # Note that while the complexity may look dangerous, this is really
        # just O(n), we make a single iteration for every value in group sizes
        for group in h:
            
            # Counting how many people we've appended to this group
            c = 0
            
            # Creating our new output group
            newOut = []
            
            # This is suprisingly O(1) keeping our complexity down
            while len(h[group]) > 0:
                newOut.append(h[group].pop())
                c += 1
                
                if c >= group:
                    out.append(newOut)
                    newOut = []
                    c = 0
                    
        return out
                
                