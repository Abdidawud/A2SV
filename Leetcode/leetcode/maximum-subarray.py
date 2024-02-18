class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum=[0]
        postfix_sum=[]
        for i in nums:
            prefix_sum.append(prefix_sum[-1]+i)
        ans=max(prefix_sum[1:])
        min_=0
        for i in range(1,len(prefix_sum)):
            ans=max(ans,prefix_sum[i]-min_)
            min_=min(min_,prefix_sum[i])
        return ans