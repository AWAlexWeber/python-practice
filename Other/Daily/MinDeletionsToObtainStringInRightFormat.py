# Given a string S of length N consisting of only letters 'A' and/or 'B'. Our goal is to obtain a string in the format
# A...AB...B (all letters A occur before all letters B) by deleting some letters from S. In particular, strings consisting only of letters A or B fit this format

# Given an example:
# S = "BAAABAB", we return 2
# S = "BBABAA", we return 3
# S = "AAAAABBB" we return 0

# We simply need to count the number of Bs before the last A, and the number of As before the first B
# Whichever number is smaller becomes our answer

# This solution is O(n) and O(1) (with a fairly high constant given two loops)
def solution(S: str) -> int:
    temporaryBCount = currentBCount = 0
    for c in S:
        if c == 'B':
            temporaryBCount += 1
        elif c == 'A':
            currentBCount = temporaryBCount

    temporaryACount = currentACount = 0
    for c in S[::-1]:
        if c == 'A':
            temporaryACount += 1
        elif c == 'B':
            currentACount = temporaryACount

    return min(currentACount, currentBCount)

print(solution("BAAABAB"))
print(solution("BBABAA"))
print(solution("AAAABBB"))
print(solution("ABBAABBABBBBBB"))

