class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans=0
        maxx=0

        for i in range(len(flips)):
            maxx=max(maxx,flips[i])
            if i+1 >= maxx and i+1 >= flips[i]:
                ans+=1
        
        return ans