class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        dic=defaultdict(int)
        dic[0]=1
        ans=0
        for i in nums:
            if i%2==1:
                prefix_sum+=1
            ans+=dic[prefix_sum-k]
            dic[prefix_sum]+=1
            
        return ans