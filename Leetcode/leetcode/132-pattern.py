class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        stack=[]
        ans=float("-inf")
        for i in range(len(nums)-1,-1,-1):
            if ans> nums[i]:
                return True
            while (stack and stack[-1]<nums[i]):
                ans=stack.pop()
            stack.append(nums[i])
        return False