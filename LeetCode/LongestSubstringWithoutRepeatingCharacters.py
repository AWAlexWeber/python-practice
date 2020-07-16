def lengthOfLongestSubstring(s: str) -> int:
    # Representations of our left and right most index
    l, r = (0,0)
    max = 0

    # Dictionary of every 'mapped' value that we have visisted
    m = {}

    iterationCount = 0

    # Expanding our window size for every increment that we do not have a match
    while r < len(s):

        iterationCount += 1

        if m.__contains__(s[r]):
            if r - l > max:
                max = r - l

            # Jumping to previous position
            l = m[s[r]] + 1
            r = l

            m = {}

        m[s[r]] = r
        r+=1

    if r - l > max:
        max = r - l

    print(iterationCount)

    return max

# 0 1 2 3 4 5 6 7
# a b c d c b a f
#       l r

# a = 0
# b = 1
# c = 2
# d = 3
#
#

# l = 0
# r = 0