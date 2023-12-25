class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=0
        li=[]
        s=max(candies)
        for i in range(len(candies)):
            ans=candies[i] + extraCandies
            if ans >= s:
                li.append(True)
            else:
                li.append(False)
        return li