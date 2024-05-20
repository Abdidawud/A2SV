# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent={i:i for i in range(len(s))}
        rank={i:1 for i in range(len(s))}

        def find(x):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            par_x=find(x)
            par_y=find(y)

            if par_x!=par_y:
                if rank[par_x]>rank[par_y]:
                    parent[par_y]=par_x
                elif rank[par_y]>rank[par_x]:
                    parent[par_x]=par_y
                else:
                    parent[par_y]=par_x
                    rank[par_y]+=1
        
        for x,y in pairs:
            union(x,y)
        for i in range(len(s)):
            find(i)
        dic=defaultdict(list)
        for i in parent:
            dic[parent[i]].append(s[i])
        for i in dic:
            dic[i].sort(reverse=True)
        ans=[]

        for i in range(len(s)):
            temp=dic[parent[i]].pop()
            ans.append(temp)
        return "".join(ans)