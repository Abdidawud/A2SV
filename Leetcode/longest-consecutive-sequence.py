class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        ans=[]
        op=0
        if nums==[]:
            return 0
        for i in range(len(nums)+1):
            if i==len(nums)-1:
                ans.append(op)
                break
            elif nums[i+1]==nums[i]+1:
                op+=1
            elif nums[i+1]==nums[i]:
                continue
            elif nums[i+1]!=nums[i]+1:
                ans.append(op)
                op=0 

        return (max(ans)+1)