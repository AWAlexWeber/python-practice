'''

Amazon wants to develop a system for identifying similar users. Given a list of information such as

(User A, Product A)
(User A, Product B)
(User B, Product A)
(User B, Product C)
(User C, Product D)

Determine which user is most similar to another user. For example, we could say user A is most similar to user B in purchasing. Break ties alphabetically.

For example:
users = [A,B,C,D,E,F]
items = [1,2,3,4]
data = [(A,1),(A,2),(A,3),(B,1),(C,1),(C,2),(C,3),(D,4),(E,2),(E,3),(F,4)]

If asked about user A, we would say user C is the most similar.
'''

from typing import List
from collections import defaultdict

# This is a topological sorting question on a bipartite graph; We will use one-mode projection, and select the highest count link.
# Complexity will be O(n * m) where n is the number of projects and m is the number of users.
# Space complexity of O(n * m), effectively because we conver the data field into two dictionaries

class Solution():
    def similarUser(self, users: List[str], products: List[str], data: List[tuple], target: str):
        # First we need to take the dataset and convert it into a hash of sets
        userProjection = defaultdict(lambda: set())
        productProjection = defaultdict(lambda: set())

        # O(n) where n is the number of datapoints in our dataset
        for p in data:
            userProjection[p[0]].add(p[1])
            productProjection[p[1]].add(p[0])

        # Now that we've constructed our sets, we're going to iterate over all of the project keys in our target set. O(n * m)
        userCount = defaultdict(lambda: 0)
        maxUserCount, maxUser = 0, None
        for product in userProjection[target]:
            for user in productProjection[product]:
                if user == target:
                    continue
                userCount[user] += 1

                # Extra bit after that or handles alphabetical ties
                if (userCount[user] > maxUserCount) or (userCount[user] == maxUserCount and user < maxUser):
                    maxUserCount = userCount[user]
                    maxUser = user

        return maxUser
        
s = Solution()
print(s.similarUser(['A','B','C','D','E','F'], [1,2,3,4], [('A',1),('A',2),('A',3),('B',1),('B',2),('C',1),('C',2),('C',3),('D',4),('E',2),('E',3),('F',4)], 'A'))