# Problem: D -  Longest Good Sequence - https://codeforces.com/gym/524965/problem/D

import sys
n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
if n == 1 and nums[0] == 1:
    print(1)
    sys.exit()

def helper(num):
    divisors = []
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)

    return divisors  

dp = [0] *(max(nums) + 1)
for num in nums:
    divisors = helper(num)
    dp[num] = 1
    for div in divisors:
        dp[num] = max(dp[num], dp[div] + 1)

    for div in divisors:
        dp[div] = max(dp[div], dp[num])
print(max(dp))