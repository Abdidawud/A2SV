class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        ans=[-1]*len(nums)
        n=len(nums)
        for i in range(2*n):
            num=nums[i%n]
            while stack and nums[stack[-1]]<num:
                ans[stack[-1]]=num
                stack.pop()
            if i< n:
                stack.append(i)
        return ans