# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent={i:i for i in range(len(strs))}
        size=[1]*len(strs)

        def find(x):
            if x==parent[x]:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            par_x=find(x)
            par_y=find(y)
            # parent[par_x]=par_y

            if par_x != par_y:
                if size[par_x]>size[par_y]:
                    parent[par_y]=par_x
                    size[par_x]+=par_y
                else:
                    parent[par_x]=par_y
                    size[par_y]+=par_x
        def helper(str1,str2):
            diff=0
            for char1,char2 in zip(str1,str2):
                if char1!=char2:
                    diff+=1
                if diff>2:
                    return False
            return True
        
        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                if helper(strs[i],strs[j]):
                    union(i,j)
        ans=0
        print(parent)
        for i in parent:
            if parent[i]==i:
                ans+=1
        return ans