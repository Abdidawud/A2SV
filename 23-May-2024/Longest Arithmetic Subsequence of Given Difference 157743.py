# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp={}
        max_=1
        
        for num in arr:
            if num-difference not in dp:
                dp[num]=1
            else:
                dp[num]=dp[num-difference]+1
            max_=max(max_,dp[num])
        return max_