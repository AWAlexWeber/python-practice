'''
Third-party companies that sell their products on Amazon.com are able to analyze the customer reviews for their products in real time. Imagine that Amazon is creating a category called "five-star sellers" that will only display products sold by companies whose average percentage of five-star reviews per-product is at or above a certain threshold. Given the number of five-star and total reviews for each product a company sells, as well as the threshold percentage, what is the minimum number of additional fivestar reviews the company needs to become a five-star seller?

For example, let's say there are 3 products (n = 3) where productRatings = [[4,4], [1,2], [3, 6]], and the percentage ratings Threshold = 77. The first number for each product in productRatings denotes the number of fivestar reviews, and the second denotes the number of total reviews. Here is how we can get the seller to reach the threshold with the minimum number of additional five-star reviews:

Before we add more five-star reviews, the percentage for this seller is ((4 / 4) + (1/2) + (3/6))/3 = 66.66%
If we add a five-star review to the second product, the percentage rises to ((4 / 4) + (2/3) +(3/6))/3 = 72.22%
If we add another five-star review to the second product, the percentage rises to ((4 / 4) + (3/4) + (3/6))/3 = 75.00%
If we add a five-star review to the third product, the percentage rises to ((4/4) + (3/4) + (4/7))/3 = 77.38%
At this point, the threshold of 77% has been met. Therefore, the answer is 3 because that is the minimum number of additional five-star reviews the company needs to become a five-star seller.
'''

from typing import List

# Hard core time-complexity of O(n*x) where x is the total number of new product reviews needed and n is products. O(n) space complexity where n is products.
class Solution():
    # Determines which increment will give us the best overall increase
    def bestIncrement(self, productRatings: List[int]) -> int:
        targetIndex, best = -1, 0
        for idx, product in enumerate(productRatings):
            # Calculating the difference
            newValue = (product[0] + 1) / (product[1] + 1)
            diff = newValue - (product[0]/product[1])
            if diff > best:
                best = diff
                targetIndex = idx
        
        return targetIndex

    def currentRatings(self, productRatings: List[int]) -> int:
        # Calculating the current product ratings
        s = 0
        for product in productRatings:
            s += (product[0]/product[1])
        return s * 100 / len(productRatings)

    def numFiveStarsNeeded(self, products: int, productRatings: List[int], threshold: int) -> int:
        # We need to calculate the current average five-star review
        count = 0
        while self.currentRatings(productRatings) < threshold:
            print(productRatings)
            count += 1
            targetIncrement = self.bestIncrement(productRatings)
            product = productRatings[targetIncrement]
            newProductScore = [product[0] + 1, product[1] + 1]
            productRatings[targetIncrement] = newProductScore


        return count

def fiveStartReviews(productRatings, ratingsThreshold):
    def currentRatings(productRatings: List[int]) -> int:
        # Calculating the current product ratings
        s = 0
        for product in productRatings:
            s += (product[0]/product[1])
        return s * 100 / len(productRatings)
        
    def bestIncrement(productRatings: List[int]) -> int:
        targetIndex, best = -1, 0
        for idx, product in enumerate(productRatings):
            # Calculating the difference
            newValue = (product[0] + 1) / (product[1] + 1)
            diff = newValue - (product[0]/product[1])
            if diff > best:
                best = diff
                targetIndex = idx
        
        return targetIndex
    
    # We need to calculate the current average five-star review
    count = 0
    while currentRatings(productRatings) < ratingsThreshold:
        print(productRatings)
        count += 1
        targetIncrement = bestIncrement(productRatings)
        product = productRatings[targetIncrement]
        newProductScore = [product[0] + 1, product[1] + 1]
        productRatings[targetIncrement] = newProductScore
    return count
        
print(fiveStartReviews([[4,4],[1,2],[3,6]], 77))
