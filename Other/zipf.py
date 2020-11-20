# ZIPFY States that 20% of the characters on your keyboard will make up 80% of the letters when typed in randomly.

from collections import Counter

s = input("Type random letters to test the zipfy theorem.\n")
s = s.lower()

h = dict(Counter(j for j in list(s)))
t = {k: v for k, v in sorted(h.items(), key=lambda item: item[1], reverse=True)}

sLen = len(s)
totalPercent = 0
valueCount = 0
for value in t:
    totalPercent += t[value] / sLen
    print(value,t[value], totalPercent)
    valueCount += 1
    if totalPercent > 0.8:
        break

print(valueCount,valueCount/len(h.keys()))