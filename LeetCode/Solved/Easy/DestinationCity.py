'''
1436. Destination City

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
 

Constraints:

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character.
'''

from typing import List

# Slow solution
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        h = set()
        d = ""
        for p in paths:
            h.add(p[0])
        for p in paths:
            if p[1] not in h:
                return p[1]

    # Slightly faster with one loop
    def fasterDestCity(self, paths: List[List[str]]) -> str:
        # Keeping track of two sets, one of the possible solutions
        # And one that has entries that have occured twice
        h = set() # All not possible options
        e = set() # All possible options
        
        # Note that by definition our only valid options for set e are second position options
        for p in paths:
            if p[1] in e and p[1] not in h:
                e.remove(p[1])
                h.add(p[1])
            elif p[1] not in h:
                e.add(p[1])
                
            if p[0] in e and p[0] not in h:
                e.remove(p[0])
                h.add(p[0])
            else:
                h.add(p[0])
                
        return e.pop()