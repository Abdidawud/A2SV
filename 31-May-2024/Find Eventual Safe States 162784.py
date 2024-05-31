# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def topsort( node, colors):
            if colors[node]==1:
                return False
            colors[node]=1
            for n in graph[node]:
                if colors[n]==2:
                    continue
                if not topsort(n,colors):
                    invalids.add(node)
                    return False
            colors[node]=2
            return True
        
        
        colors=[0 for _ in range(len(graph))]
        
        ans=[]
        invalids=set()

        for node in range(len(graph)):
            if colors[node]!=0:
                continue
            topsort(node,colors)
        ans=[]
        for i in range(len(graph)):
            if i not in invalids:
                ans.append(i)
        return ans