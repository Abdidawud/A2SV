# Problem: C - Coffee Dilemma - https://codeforces.com/gym/528792/problem/C

import heapq
n = int(input())
a = [int (i) for i in input().split()]
li= []
total_sum = 0
for i in a:
	total_sum += i
	heapq.heappush(li, i)
	while total_sum < 0:
		total_sum -= heapq.heappop(li)
print(len(li))