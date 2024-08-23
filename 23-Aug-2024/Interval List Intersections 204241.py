# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans=[]

        for i in firstList:
            for j in secondList:
                temp=[]
                temp.append(max(j[0],i[0]))
                
                if min(j[1],i[1])>=temp[0]:
                    temp.append(min(j[1],i[1]))
                    ans.append(temp)
                else:
                    continue
        
        return ans