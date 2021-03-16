'''
Given an array of numbers, combine them to create the largest potential number.
'''

from functools import cmp_to_key

def largestNum(nums):
  sorted_nums = sorted(nums, key=cmp_to_key(
      lambda a, b:
      1 if str(a) + str(b) < str(b) + str(a)
      else -1)
  )
  return ''.join(str(n) for n in sorted_nums)


print(largestNum([17, 7, 2, 45, 72]))