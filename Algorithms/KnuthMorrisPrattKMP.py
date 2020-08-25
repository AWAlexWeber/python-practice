# KMP is an incredibly strong pattern searching algorithm
# Essentially, given a text and a pattern, return all occurences of pattern in text
# This ends up giving us an O(M+N) search time versus O(M*N) (where m is length of input, and n is length of pattern)

# Basically, by knowing that we have a certain number of subcases and the fact that we know the characters in the next subwindow, we can just skip to the next proper window
# The first part is the preprocessing pattern

# Preprocessing basically returns an array where each index is equal to how wide a mirror is
# if we take a look at
# a a b a a b x a a b
# 0 1 0 1 2 3 0 1 2 3

def rewritepreprocess(pat: str) -> str:
    lps = [0] * len(pat)
    i, j = 1, 0

    while i < len(pat):
        if pat[i] == pat[j]:
            lps[i] = lps[i-1] + 1
            j += 1
        else:
            if j != 0:
                # Move j back one
                j = lps[j - 1]
                
            j = 0
            lps[i] = 0
        
        i += 1

    return lps

print(rewritepreprocess("aabaabxaab"))

def preprocess(pat: str) -> str:
    lps = [0] * len(pat)
    i, j = 1, 0
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < len(pat): 
        if pat[i]== pat[j]: 
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0: 
                j = lps[j-1] 

            else: 
                lps[i] = 0
                i += 1

    return lps


from typing import List

# The actual searching algorithm
def kmpsearch(txt: str, pat: str) -> List[int]:
    o = []

    # Defining lengths
    n, m = len(txt), len(pat)

    # Preprocessing
    lps = preprocess(pat)
    print(lps)

    # Iterating
    i = j = 0

    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        
        if j == m:
            # Match found!
            o.append(i-m)

            # Moving our starting j value to the beginning of the lps
            j = lps[j-1]

        # Mismatch
        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

    return o

print("Performing KMP Search")
print(kmpsearch("aabaabxaabaabxaabaabxaabaabxaabaabaabaabxaab", "aabaabxaab"))