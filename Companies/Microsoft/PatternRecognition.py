'''
Given a pattern as the first argument and a string of blobs split by | show the number of times the pattern is present in each blob and the total number of matches.

Input:
The input consists of the pattern (“bc” in the example) which is separated by a semicolon followed by a list of blobs (“bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32” in the example). Example input: bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32

Output:
The output should consist of the number of occurrences of the pattern per blob (separated by |). Additionally, the final entry should be the summation of all the occurrences (also separated by |).

Example output: 3|2|1|2|8 where ‘bc’ was repeated 3 times, 2 times, 1 time, 2 times in the 4 blobs passed in. And 8 is the summation of all the occurrences (3+2+1+2 = 8)

Test 1
bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32

Expected Output
3|2|1|2|8

Test 2
aa;aaaakjlhaa|aaadsaaa|easaaad|sa

Expected Output
4|4|2|0|10

Test 3
b;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32
Expected Output
4|2|3|2|11

Test 4
;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32
Expected Output
0|0|0|0|0
'''

from typing import List

class Solution:
    def patternRecognizer(self, s: str) -> int:
        # Determining our pattern to match against
        pattern = s[:s.index(';')]

        if len(pattern) <= 0:
            return 0

        # Using KMP to pre-process the pattern.
        preProc = self.kmpPreProcess(pattern)

        # Then, for each split we perform pattern recongition up to each |.
        # Note we could use split or something similar here, but this keeps our constant lower

        # Tracking our total count.
        outputCount = list()
        maxCount = 0
        totalCount = 0
        patternIndex = 0

        for i in range(len(pattern) + 1, len(s)):
            c = s[i]

            # Resetting when we hit a block
            if c == '|':
                outputCount.append(str(str(totalCount) + "|"))
                maxCount += totalCount
                totalCount = 0
                patternIndex = 0
                continue

            # Attempting to perform a match
            if s[i] == pattern[patternIndex]:
                patternIndex += 1

                # If we're at the end, we can create a total count, then reset our pattern index
                if patternIndex == len(pattern):
                    totalCount += 1
                    patternIndex = 0

                continue

            elif s[i] != pattern[patternIndex]:
                if patternIndex != 0:
                    patternIndex = preProc[patternIndex - 1]

        outputCount.append(str(str(totalCount) + "|"))
        maxCount += totalCount
        outputCount.append(maxCount)
        return ''.join([str(e) for e in outputCount])

    # KMP Preprocess
    def kmpPreProcess(self, p: str) -> List[int]:
        # Returns a list of our skip index.
        preProc = [0] * len(p)
        i, j = 1, 0

        # Iterating through all possible values of p. Note by starting at 1, we skip any string of size 1.
        while i < len(p):
            if p[i] == p[j]:
                j += 1
                preProc[i] = j
                i += 1
            else:
                if j != 0:
                    j = preProc[j - 1]
                else:
                    preProc[j] = 0
                    i += 1

        return preProc



s = Solution()
print(s.patternRecognizer('b;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32'))