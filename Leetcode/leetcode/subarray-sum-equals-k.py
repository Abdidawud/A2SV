class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=Counter()
        count[k]=1
        ans=0
        prefix_sum=[0]*(len(nums)+1)

        for i in range(1,len(nums)+1):
            prefix_sum[i]=prefix_sum[i-1]+nums[i-1]
            if count[prefix_sum[i]]>0:
                ans+=count[prefix_sum[i]]
            count[prefix_sum[i]+k]+=1
            
        return ans