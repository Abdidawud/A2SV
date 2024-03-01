class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_sum=nums
        prefix_sum=[0]+prefix_sum
        for i in range(1,len(prefix_sum)):
            prefix_sum[i]=prefix_sum[i]+prefix_sum[i-1]
        rem=prefix_sum[-1]% p
        if rem==0:
            return 0
        
        dic = {}
        ans = float('inf')
        for i in range(len(prefix_sum)):
            x = prefix_sum[i] % p
            if x in dic:
                ans = min(ans, i - dic[x])
            dic[(rem + x) % p] = i
        if ans == float('inf') or ans == len(prefix_sum) - 1:
            return -1
        return ans