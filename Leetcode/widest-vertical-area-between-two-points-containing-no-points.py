class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        k=sorted(points , key=lambda item:item[0])
        li=[k[i+1][0]-k[i][0] for i in range(len(k)-1)]
        
        return (max(li))