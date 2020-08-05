# Implement a method to perform basic string compression using the counts of repeated characters. If the compressed string would be longer than the input string, return the input string

# Note that using a string array and then combining it together is much faster than adding to an array
def compress(s: str):
    if len(s) <= 0:
        return s

    d, n, o = 1, s[0], [""] * len(s)
    for i, c in enumerate(s[1:]):
        if n == c:
            d += 1

        elif n != c:
            o[i] = (n + str(d))
            d, n = 1, c 

    # Processing the last digit
    o[i + 1] = (n + str(d))
    
    o = ''.join(o)
    if len(o) >= len(s):
        return s
    else:
        return o

# Test cases 
testCases = ["abcdefg","aabbccddeeffgg","abel","","aaaaaaaaaaaaaaaaaaa", "aabbccddeeffgghh","aabbcccccccccd"]
for t in testCases:
    print(compress(t))