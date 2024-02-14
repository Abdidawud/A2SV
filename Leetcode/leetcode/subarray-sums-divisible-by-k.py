class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        ans=0
        acc=0

        for i in range(len(nums)):
            acc+=nums[i]
            temp=acc % k
            if temp in dic:
                ans += dic[temp]
            dic[temp] +=1
        
        return ans