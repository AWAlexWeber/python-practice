'''

'''

# This solution handles non-duplicate characters
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        characterIndexMap = {}
        characterSetMap = set()
        currentBestLength, currentBestString = float('inf'), ""
        
        # Building our comparison set
        comparisonSet = set(t)
        
        for i in range(0, len(s)):
            c = s[i]
            if c in comparisonSet:
                characterIndexMap[c] = i
            
            if c not in characterSetMap and c in comparisonSet:
                characterSetMap.add(c)
                
            # Do we have enough to start making our calculations?
            if len(characterSetMap) == len(t):
                # Calculate minimal and maximal values 
                mini, maxi = float("inf"), float("-inf")
                
                for k in characterIndexMap.keys():
                    if characterIndexMap[k] < mini:
                        mini = characterIndexMap[k]
                    if characterIndexMap[k] > maxi:
                        maxi = characterIndexMap[k]
                        
                if maxi - mini < currentBestLength:
                    currentBestLength = (maxi - mini)
                    currentBestString = s[mini:maxi + 1]
                    
        return currentBestString

from collections import Counter

# Handles duplicates
class SolutionDuplicates:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t)

        required = len(dict_t)

        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        l, r = 0, 0
        formed = 0
        window_counts = {}

        ans = float("inf"), None, None

        # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
        # Hence, we follow the sliding window approach on as small list.
        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1

            if window_counts[character] == dict_t[character]:
                formed += 1

            # If the current window has all the characters in desired frequencies i.e. t is present in the window
            while l <= r and formed == required:
                character = filtered_s[l][1]

                # Save the smallest window until now.
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1    

            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]