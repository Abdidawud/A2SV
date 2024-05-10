# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree=[0]*n
        for a,b in edges:
            indegree[b]+=1
        li=[]
        for i in range(n):
            if indegree[i]==0:
                li.append(i)
        return li[0] if len(li)==1 else -1