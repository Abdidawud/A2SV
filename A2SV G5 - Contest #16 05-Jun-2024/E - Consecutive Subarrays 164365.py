# Problem: E - Consecutive Subarrays - https://codeforces.com/gym/523525/problem/E

n,k=(int(i) for i in input().split())
li=[int(i) for i in input().split()]
s_sum=[0]
for i in range(n-1,-1,-1):
    s_sum.append(s_sum[-1]+li[i])
s_sum=s_sum[::-1]
s_sum.pop()
if k-1==0:
    print(s_sum[0])
else:
    print(s_sum[0]+ sum(sorted(s_sum[1:])[-k+1:]))