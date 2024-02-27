class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans=0
        li=sorted(costs, key=lambda x: x[0]-x[1])
        for i in range(len(li)//2):
            ans+=li[i][0]
        for i in range(len(li)//2,len(li)):
            ans+=li[i][1]
        return ans