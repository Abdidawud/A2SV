# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        li=[]
        for i in range(n):
            li.append([efficiency[i],speed[i]])
        li.sort(reverse=True)

        heap=[]
        ans=0
        _sum=0
        for i in range(n):
            _sum +=li[i][1]
            if len(heap)<k:
                heappush(heap,[li[i][1],li[i][0]])
            else:
                _sum-=heappop(heap)[0]
                heappush(heap,[li[i][1],li[i][0]])
            ans=max(ans,_sum*li[i][0])
        return ans%((10**9)+7)