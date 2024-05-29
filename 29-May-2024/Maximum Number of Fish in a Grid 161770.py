# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited=set()
        dir=[[0,1],[1,0],[-1,0],[0,-1]]
        max_=0
        def helper(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return False
            if grid[i][j]==0:
                return False
            if (i,j) in visited:
                return False
            
            return True
        
        def bfs(i,j):
            nonlocal max_
            sum_=grid[i][j]
            q=[(i,j)]
            while q:
                x,y=q.pop()
                for i,j in dir:
                    new_r=x+i
                    new_c=y+j
                    
                    if helper(new_r,new_c):
                        sum_+=grid[new_r][new_c]
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
            max_=max(max_,sum_)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0 and (i,j) not in visited:
                    visited.add((i,j))
                    bfs(i,j)
        return max_
