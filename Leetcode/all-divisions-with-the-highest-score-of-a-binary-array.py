class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dic=defaultdict(list)
        high=0
        sum1=sum(nums)
        sum2=0

        for i in range(len(nums)+1):
            if i>0:
                if nums[i-1]==1:
                    sum1-=1
                if nums[i-1]==0:
                    sum2+=1
            total=sum1+sum2
            

            dic[total].append(i)
            if total>high:
                high=total
            

        return dic[high]