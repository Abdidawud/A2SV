# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent={i:i for i in range(len(stones))}
        rank={i:1 for i in range(len(stones))}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            par_x=find(x)
            par_y=find(y)

            if par_x != par_y:
                if rank[par_x]>rank[par_y]:
                    parent[par_y]=par_x
                elif rank[par_x]<rank[par_y]:
                    parent[par_x]=par_y
                else:
                    parent[par_y]=par_x
                    rank[par_x]+=1
        
        for i in range(len(stones)-1):
            for j in range(i+1,len(stones)):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    # print(i,j)
                    union(i,j)
        
        for i in parent:
            find(i)
        ans=0
        for i in parent:
            if i != parent[i]:
                ans+=1
        # print(parent)
        # print(rank)
        return ans