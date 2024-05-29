# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        dp=[[float("inf")]*(1<< n) for _ in range(n)]
        dp.append([0]*(1<< n) )
        for idx1 in range(n-1,-1,-1):
            for mask in range((1<<n)-1,-1,-1):
                min_xor=float("inf")

                for i in range(n):
                    if mask&(1<<i)==0:
                        min_xor=min(min_xor,(nums1[idx1]^nums2[i])+dp[idx1+1][mask | (1<<i)])
                dp[idx1][mask]=min_xor
        return dp[0][0]