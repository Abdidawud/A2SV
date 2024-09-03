# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans=[]
        if m*n==len(original):
            i=0
            while i <len(original):
                temp=[]
                for j in range(i,i+n):
                    temp.append(original[j])
                i+=n
                ans.append(temp)
            return ans

        return []