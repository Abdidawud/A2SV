# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        prefix_xor=[0]
        for i in arr:
            prefix_xor.append(prefix_xor[-1]^i)
        # print(prefix_xor)
        for i,j in queries:
            ans.append(prefix_xor[i]^prefix_xor[j+1])
        return ans