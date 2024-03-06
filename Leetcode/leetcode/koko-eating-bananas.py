class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        best=max(piles)
        while left<=right:
            mid=(left+right)//2

            time=0
            for i in range(len(piles)):
                time+=ceil(piles[i]/mid)
            
            if time>h:
                left=mid+1
            else:
                right=mid-1
                best=mid
        return best