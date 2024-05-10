# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        def inbound(row,col):
            return 0<=row<len(board) and 0<=col<len(board[0])
        
        def dfs(row,col):
            if not inbound(row,col) or board[row][col]!="O":
                return 
            if board[row][col]=="O":
                board[row][col]="T"
            for i,j in dir:
                new_r=row+i
                new_c=col+j
                dfs(new_r,new_c)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1) and board[i][j]=="O":
                    dfs(i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="T":
                    board[i][j]="O"