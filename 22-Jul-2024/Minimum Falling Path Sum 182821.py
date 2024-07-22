# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        one=float("inf")
        two=float("inf")
        three=float("inf")

        for i in range(1,len(matrix)):
            for j in  range(len(matrix[0])):
                if j>0:
                    one=matrix[i-1][j-1]
                else:
                    one=float("inf")
                if j<len(matrix[0])-1:
                    two=matrix[i-1][j+1]
                else:
                    two=float("inf")
                three=matrix[i-1][j]

                matrix[i][j]+=min(one,two,three)
        return min(matrix[-1])
                