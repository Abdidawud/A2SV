class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum=[0]*len(nums)
        postfix_sum=[0]*len(nums)
        _sum=1
        for i in range(len(nums)):
            _sum*=nums[i]
            prefix_sum[i]=_sum
        _sum=1
        for i in range(len(nums)-1,-1,-1):
            _sum*=nums[i]
            postfix_sum[i]=_sum
        
        ans=[]
        for i in range(len(nums)):
            if i==0:
                ans.append(postfix_sum[i+1])
            elif i==len(nums)-1:
                ans.append(prefix_sum[i-1])
            else:
                ans.append(postfix_sum[i+1]*prefix_sum[i-1])
        return ans