# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        indegree=[0 for i in range(n)]
        
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
            indegree[i]+=1
            indegree[j]+=1
        # print(graph)
        # print(indegree)
        q=deque()
        for i in range(len(indegree)):
            if indegree[i]==1:
                q.append(i)
        if n<3:
            return [i for i in range(n)]

        while n>2:
            bound=len(q)
            n-=bound
            for i in range(bound):
                node=q.popleft()
                for i in graph[node]:
                    indegree[i]-=1
                    if indegree[i]==1:
                        q.append(i)
                    
        q=set(q)
        return list(q)