class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        i=0
        j=0
        arrows=0
        while i <len(points):
            while j<len(points) and points[i][1]>=points[j][0]:
                j+=1
            i=j
            arrows+=1
        return arrows


