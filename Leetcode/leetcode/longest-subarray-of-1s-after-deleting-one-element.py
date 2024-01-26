class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        dic=defaultdict (int)
        first=0
        second=0
        maxx=0

        while second< len(nums):
            dic[nums[second]]+=1

            if dic[nums[second]]>1 and nums[second]==0:
                while dic[nums[second]]>1:
                    dic[nums[first]]-=1
                    first+=1

            second+=1
            maxx=max(maxx,(second-first))
        
        return (maxx-1)