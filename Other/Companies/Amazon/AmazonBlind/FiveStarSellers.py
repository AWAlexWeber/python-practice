'''

'''

from heapq import heappush, heappop
import heapq
from typing import List

class Solution():
    def fiveStarSellers(self, productRatings: List[tuple], ratingThreshold: int) -> int:
        # Time complexity: O(nlogm) where n is the number of reviews needed to meet the ratingThreshold, m is the number of products.
        # Space complexity: O(k) where k is the number of products, due to our heap
        # We are going to solve this by keeping a minheap with what an increase would do for our rating
        # First we have to calculate our current rating
        ratingThreshold /= 100
        rating = 0
        for fiveStarReviews, totalReviews in productRatings:
            rating += (fiveStarReviews/totalReviews)
        rating /= len(productRatings)

        # Now we will use our heap while we have a rating below the ratingThreshold.
        # First we need to build our heap
        heap = list()

        for fiveStarReviews, totalReviews in productRatings:
            # Calculating the difference
            scoreGap = ((fiveStarReviews + 1) / (totalReviews + 1)) - ((fiveStarReviews) / (totalReviews))
            scoreGap /= len(productRatings)
            heapq.heappush(heap, (-scoreGap, (fiveStarReviews + 1, totalReviews + 1)))

        # Alright now we actually use our heap
        increaseCount = 0
        while rating < ratingThreshold:
            v = heapq.heappop(heap)
            increaseCount += 1
            score, review = (v)
            rating += (-score)
            fiveStarReviews, totalReviews = (review)
            scoreGap = ((fiveStarReviews + 1) / (totalReviews + 1)) - ((fiveStarReviews) / (totalReviews))
            scoreGap /= len(productRatings)
            heapq.heappush(heap, (-scoreGap, (fiveStarReviews + 1, totalReviews + 1)))

        return increaseCount

s = Solution()
print(s.fiveStarSellers([[1,4],[1,2],[1,6]], 77))
