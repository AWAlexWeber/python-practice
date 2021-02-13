'''
Taken from leetcode here https://leetcode.com/discuss/interview-question/785229/google-phone-interview-question
There are N different packages. the ith package is of X[i] days and the price of that package is Y[i]. 
There are M customers. the jth customer wants the package of at least A[j] days and he doesn't want to spend more than B[j] for any package. 
One package can accommodate at most one customer and a customer can buy at most one package. 

You have to find the maximum number of packages, you can sell.
'''

from typing import List

class Solution():

    def totalCustomers(self, n: int, x: List[int], y: List[int], m: int, a: List[int], b: List[int]):
        # First we perform counting sort across x, while swapping the same indexes in y

        # Now we perform counting sort across a, while swapping the same indexes in b
        # Given that this is quicksort, we have a space complexity of O(log(n)) and a time complexity of O(n log(n)) + O(m log(m)) (assuming this is not one of the worse-cases for quicksort. If it is, then its O(n^2))
        # We assume that the input is randomized and does not have any strange patterns (such as inverse ordering) that would make quicksort run poorly.
        self.quicksortPair(x,y,0,n)
        self.quicksortPair(a,b,0,m)

        print(x,y)
        print(a,b)

        # Now we sort the values within the pair arrays when the values in the parent arrays are equal
        # This ensures that we properly select valid packages later

        # The worse case for this is the exact same as sorting for x,y. Our constant increases but our total time complexity stays the same
        i = l = 0
        for i in range(n):
            if not x[i] == x[l]:
                # Attempting sort if size is large enough
                if i - l > 1:
                    self.quicksortPair(y,None,l,i)
                l = i
        i += 1

        if i - l > 1:
            self.quicksortPair(y,None,l,i)


        i = l = 0
        for i in range(m):
            if not a[i] == a[l]:
                # Attempting sort if size is large enough
                if i - l > 1:
                    self.quicksortPair(b,None,l,i)
                l = i
        i += 1

        if i - l > 1:
            self.quicksortPair(b,None,l,i)

        print(x,y)
        print(a,b)

        # While we have a valid customer we decrement both
        # While we have an invalid customer, we decrement our package
        # Essentially as we know that in order for the customer to be valid both X[i] and Y[i] must fulfill this criteria, as x is sorted we know that whatever comes after x will not work for what is currently at x
        
        # i represents our customer index
        # j represents our package index

        # For a package j that matches the customer i requirements, we move on to the next package and customer
        # Otherwise, if the package does not satisfy the customer, we move onto the next package and stay on the customer
        i, j = m - 1, n - 1
        o = 0

        while i >= 0 and j >= 0:
            if x[j] <= a[i] and y[j] <= b[i]:

                i, o, j = i - 1, o + 1, j - 1
                
            else:
                j -= 1

        return o

    def quicksortPair(self, a: List[int], b: List[int], l: int, r: int):

        if r - l <= 1:
            return 

        # Quicksort
        i, j, p = l, l - 1, r - 1

        while i < p:
            # Attempting to swap around pivot
            if a[i] <= a[p]:
                j += 1
                if not i == j:
                    # Perform swap
                    a[i], a[j] = a[j], a[i]
                    if b:
                        b[i], b[j] = b[j], b[i]

            i += 1

        # Final swap with the pivot index
        j += 1
        a[p], a[j] = a[j], a[p]
        if b:
            b[p], b[j] = b[j], b[p]

        # Quicksort to the left and right
        self.quicksortPair(a, b, l, p)
        self.quicksortPair(a, b, j, r)

x = [1,1,1,1,1,1]#[5, 25, 15, 1, 2, 3, 4, 5, 6]
y = [10,11,12,13,14,15]#[5, 10, 8, 8, 9, 2, 4, 9, 3]
n = len(x)

a = [1,1,1,1,1,1]#[5, 10, 30, 18, 5, 10, 3]
b = [15,14,13,12,11,10]#[5, 30, 15, 15, 3, 2, 1]
m = len(a)

s = Solution()
print(s.totalCustomers(n,x,y,m,a,b))