'''
Amazon Online Assessment (OA) - Top K Frequently Mentioned Keywords
Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to least frequently mentioned.

The comparison of strings is case-insensitive.

Multiple occurances of a keyword in a review should be considred as a single mention.

If keywords are mentioned an equal number of times in reviews, sort alphabetically.

Input
The input consists of three arguments:

k: an integer

keywords: a list of strings representing the keywords

reviews: a list of strings that consists of space-sperated words representing sentences

Output
Return a list of strings of most popular k keywords in order of most to least frequently mentioned

Examples
Example 1:
Input:
k = 2

keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]
Output: ["anacell", "betacellular"]
Explanation:
anacell is occuring in 2 different reviews and betacellular is only occuring in 1 review.

Examples
Example 2:
Input:
k = 2

keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
Output: ["betacellular", "anacell"]
'''

from typing import List

class Solution():
    def topKFrequentKeywords(self, k: int, keywords: List[str], reviews: List[str]) -> List[str]:
        # Basically we need to get the counts for each keyword in keywords.
        # Then we sort those by value, and return the final digits
        
        # First doing some minor conversions to reduce complexities later. Moving keywords into a dictionary to track total occurences.
        # O(keywords)
        keywordOccurence = {}
        for keyword in keywords:
            keywordOccurence[keyword.lower()] = 0

        # This first bit is O(words) where words is each word in each review. Note that we also apply string matching against each keyword, but since its dictionary based
        # we get (amortized) O(1) assuming our hash function is not terrible
        for review in reviews:
            # Visit set to ensure we don't count the same word multiple times a review
            visit = set()
            for word in review.split(' '):
                # We split words by spaces since we do not count misspellings.
                if word.lower() in keywordOccurence and word.lower() not in visit:
                    keywordOccurence[word.lower()] += 1
                    visit.add(word.lower())

        # Alright, we've succesfully counted the total amounts. What we are going to do is put both the index and name into a list of tuples then sort that list on both indx.
        listOfKeywords = list()
        for key in keywordOccurence.keys():
            listOfKeywords.append( (keywordOccurence[key], key))

        # Now sorting it. This takes O(nlogn) time where n is the length of our list of keywords.
        # Note that since the list of keywords has a maximum size of keywords, n is keywords
        listOfKeywords.sort(key=lambda element: (-element[0], element[1]))
        return([y for x, y in listOfKeywords[:k]])

        # Total time complexity: Total space complexity:

s = Solution()
f = s.topKFrequentKeywords(2, ['hello','there','apple'],['hello','ehello there','hello there','hello','there','there hello','apple apple apple apple'])
print(f)

k = 2

keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

s = Solution()
f = s.topKFrequentKeywords(k, keywords, reviews)
print(f)

k = 2

keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

s = Solution()
f = s.topKFrequentKeywords(k, keywords, reviews)
print(f)
