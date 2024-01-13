class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        for i in range(len(mat)):
            if i!=len(mat)-1-i:
                sum+=(mat[i][i]+mat[i][len(mat)-1-i])    
            else:
                sum+=mat[i][i]
        return sum
        
        