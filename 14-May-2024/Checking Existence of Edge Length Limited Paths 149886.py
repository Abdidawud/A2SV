# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        edgeList=sorted(edgeList,key=lambda x:x[2])
        parent={i:i for i in range(n)}
        size=[i for i in range(n)]
        
        for i in range(len(queries)):
            queries[i].append(i)
        queries=sorted(queries,key=lambda x:x[2])
        
        def find(x):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parentX=find(x)
            parentY=find(y)

            if parentX != parentY:
                if size[parentX]>size[parentY]:
                    parent[parentY]=parentX
                    size[parentX]+=size[parentY]
                else:
                    parent[parentX]=parentY
                    size[parentY]+=size[parentX]
        
        i=0
        ans=[False for i in range(len(queries))]

        for j in range(len(queries)):
            while i<len(edgeList) and queries[j][2]>edgeList[i][2]:
                union(edgeList[i][0],edgeList[i][1])
                i+=1
            if find(queries[j][0])==find(queries[j][1]):
                ans[queries[j][3]]=True
        return ans