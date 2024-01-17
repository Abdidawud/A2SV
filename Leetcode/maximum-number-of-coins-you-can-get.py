class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        i=1
        rep=len(piles)//3
        ans=0

        while rep>0:
            ans+=piles[i]
            i+=2
            rep-=1
            
        return ans