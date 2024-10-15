# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_=max(nums)
        i=0
        max_leng=0
        while i <len(nums):
            if nums[i]!=max_:
                i+=1
                continue
            temp_length=0
            while i <len(nums) and nums[i]==max_:
                temp_length+=1
                i+=1
                max_leng=max(temp_length,max_leng)
        return max_leng
