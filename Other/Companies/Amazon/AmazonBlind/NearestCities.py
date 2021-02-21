'''
Nearest Cities
There are multiple cities within a large geographic region. The cities are arranged on a graph that has been divided up like an ordinary Cartesian plane. Each city is located at an integral (x, y) coordinate intersection. City names and locations are given in the form of three arrays: c, x, and y. Which are aligned by the index to provide the city name (c[i]), and its coordinates, (x[i], y[i]).

Write an algorithm to determine the name of the nearest city that shares either an x or a y coordinate with the queried city. If no other cities share an x or y coordinate, return NONE. If two cities have the same distance to the queried city, q[i], consider the one with an alphabetically smaller name (i.e. 'ab' < 'aba' < 'abb') as the closest choice.

The distance is denoted on a Euclidean plane: the difference in x plus the difference in y.

Input
The input consists of six arguments:

numOfCities: an integer representing the number of cities

cities: a list of strings representing the names of each city [i]

xCoordinates: a list of integers representing the X coordinates of each city[i]

yCoordinates: a list of integers representing the Y-coordinates of each city[i]

numOfQueries: an integer representing the number of queries

queries: a list of strings representing the names of the queried cities

Output
Return a list of strings representing the name of the nearest city that shares either an x or a y coordinate with the queried city.

Note
Each character of all c[i] and q[i] is in the range ascii [a-z, 0-9,-].

All city name values, c[i], are unique. All cities have unique coordinates.

Constraints
1 <= numOfCities, numOfQueries < 10^5

1 < xCoordinates[i], yCoordinates[i] <= 10^9

1 < length of queries[i] and cities[i] <= 10

Examples
Example 1:
Input:
numOfCities = 3

cities = ["c1", "c2","c3"]

xCoordinates = [3, 2, 1]

yCoordinates = [3, 2, 3]

numOfQueries = 3

queries = ["c1", "c2", "c3"]

Output: ["c3", NONE, "c1"]
Explanation:
There are three points (3,3), (2,2) and (1,3) represent the coordinates of the cities on the graph. The nearest city to c1 is c3, which shares a y value (distance = (3-1) + (3-3) = 2). City c2 does not have the nearest city as any share an x or y with c2, so this query returns NONE. A query of c3 returns c1 based on the first calculation. The returned array after all queries are complete is [c3, NONE, c1].

Example 2:
Input:
numOfCities = 5

cities = ["green", "red","blue", "yellow", "pink"]

xCoordinates = [100, 200, 300, 400, 500]

yCoordinates = [100, 200, 300, 400, 500]

numOfQueries = 5

queries = ["green", "red", "blue", "yellow", "pink"]

Output: [NONE, NONE, NONE, NONE, NONE]
'''

from typing import List

class Solution():
    def nearestCity(self, cities: List[str], xCoordinates: List[int], yCoordinates: List[int], queries: List[str]):
        # Straightforward problem. Time complexity will be O(nk) where n is the number of queries and k is the number of cities.
        # This is (likely?) the best case. Might be able to apply some sort of binary search to make it faster?

        # First mapping cities to x/y coordinate for easier searching
        citiyDictionary = {}
        for idx, city in enumerate(cities):
            citiyDictionary[city] = (xCoordinates[idx], yCoordinates[idx])

        # Alright, now performing our searches on queries
        output = list()

        for query in queries:
            output.append(self.performQuery(query, citiyDictionary))

        return output

    def performQuery(self, city: str, cityDictionary: dict) -> str:
        # We will find cities that have a matching x or y coordinate then make a 'euclidian' distance check, but its really just subtracting the values.
        # Remember we need to track alphabetic nature. Simple comparison though to make that happen.
        targetX, targetY = cityDictionary[city][0], cityDictionary[city][1]
        minimalDistance, minimumCity = float('inf'), None
        for cityName in cityDictionary.keys():
            if cityName == city:
                continue
            cityX, cityY = cityDictionary[cityName]
            targetDistance = float('inf')
            if cityX == targetX:
                targetDistance = abs(cityY - targetY)

            if cityY == targetY:
                targetDistance = abs(cityX - targetX)   

            if targetDistance < minimalDistance:
                minimalDistance = targetDistance
                minimumCity = cityName

            if targetDistance == minimalDistance and minimumCity and cityName < minimumCity:
                minimumCity = cityName
        return minimumCity

s = Solution()
print(s.nearestCity(['c1','c2','c3'], [3,2,1], [3,2,3], ['c1','c2','c3']))
print(s.nearestCity(["green", "red","blue", "yellow", "pink"], [100, 200, 300, 400, 500], [100, 200, 300, 400, 500], ["green", "red", "blue", "yellow", "pink"]))