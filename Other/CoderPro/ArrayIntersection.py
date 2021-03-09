''' Given two arrays, find the values that occur in both arrays '''

from typing import List

class Solution:
    def arrayIntersection(self, list1: List[int], list2: List[int]) -> List[int]:
        def hash(list1: List[int], list2: List[int]) -> List[int]:
            # Hashing approach; we hash each value and then return the overlap.

            # This uses O(n) time and O(n) space. 
            s1, s2 = set(list1), set(list2)
            output = list()
            for value in s1:
                if value in s2:
                    output.append(value)
            return output

        def sortIntersection(list1: List[int], list2: List[int]) -> List[int]:
            # First we sort both arrays in O(nlogn) time.
            # This approach actually also uses O(n) space either way because of the return array.
            list1.sort()
            list2.sort()

            # We increment through the array, making sure that we increment whichever value is smaller. On overlaps, we insert into a list and increment both
            idx1, idx2 = 0, 0
            output = set()
            while idx1 < len(list1) and idx2 < len(list2):
                if list1[idx1] == list2[idx2]:
                    output.add(list1[idx1])
                    idx1, idx2 = idx1 + 1, idx2 + 1
                else:
                    if list1[idx1] > list2[idx2]:
                        idx2 += 1
                    else:
                        idx1 += 1

            return list(output)


        return sortIntersection(list1, list2)

s = Solution()
print(s.arrayIntersection([4,9,5],[9,4,9,8,4]))