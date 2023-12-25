class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons=0
        maxx=0

        for i in nums:
            if i==1:
                cons+=1
                maxx=max(maxx,cons)
            else:
                cons=0
        return maxx