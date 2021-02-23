'''

'''

def optimizeMemoryUsage(a, b, target):
	a.sort(key=lambda x: x[1])
	b.sort(key=lambda x: x[1])
	l, r = 0, len(b) - 1
	ans = []
	curDiff = float('inf')
	while l < len(a) and r >= 0:
		id1, i = a[l]
		id2, j = b[r]
		if (target - i - j == curDiff):
			ans.append([id1, id2])
		elif (i + j <= target and target - i - j < curDiff):
			ans.clear()
			ans.append([id1, id2])
			curDiff = target - i - j
		if (target > i + j):
			l += 1
		else:
			if target == i + j:
				tmp_l = l
				while a[tmp_l][1] + b[r][1] == target:
					tmp_l += 1
					if tmp_l == len(a):
						break
					if  a[tmp_l][1] + b[r][1] == target:
						ans.append([a[tmp_l][0], b[r][0]])
			r -= 1
	
	ans.sort(key = lambda x: x[1])
	ans.sort(key = lambda x: x[0])
	return ans

print(optimizeMemoryUsage([1,7,2,4,7,7,7,6],[3,1,2,2],9))
print(optimizeMemoryUsage([6,6],[1,1,1,1,1],7))