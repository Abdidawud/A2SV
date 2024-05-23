# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        store={}
        def dp(i,j):
            if i == len(triangle)-1:
                return triangle[i][j]
            
            if (i,j) in store:
                return store[(i,j)]
            one=triangle[i][j]+dp(i+1,j)
            two=triangle[i][j]+dp(i+1,j+1)
            store[(i,j)]=min(one,two)
            return store[(i,j)]
        return dp(0,0)