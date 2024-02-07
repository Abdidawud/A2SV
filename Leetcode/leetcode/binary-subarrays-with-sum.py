class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic=defaultdict(int)
        dic[0]+=1
        ps=[]
        ans=0
        acc=0
        for i in range(len(nums)):
            acc+=nums[i]
            ps.append(acc)
        for i in ps:
            ans+=dic[(i-goal)]
            dic[i]+=1
        return ans