# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent={}
        names={}
        size=defaultdict(int)
        
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                parent[accounts[i][j]]=accounts[i][j]
                names[accounts[i][j]]=accounts[i][0]
        # print(parent)
        def find(x):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            parentX=find(x)
            parentY=find(y)
            if parentX != parentY:
                if size[parentX] > size[parentY]:
                    parent[parentY]=parentX
                    size[parentX]+=size[parentY]
                else:
                    parent[parentX]=parentY
                    size[parentY]+=size[parentX]
        for i in range(len(accounts)):
            for j in range(2,len(accounts[i])):
                x=accounts[i][j]
                y=accounts[i][j-1]
                union(x,y)
        # print(parent)
        set_=defaultdict(set)
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                set_[find(accounts[i][j])].add(accounts[i][j])
        # print(set_)

        ans=[]
        for key,value in set_.items():
            temp=[names[key]]
            value=sorted(value)
            temp.extend(value)
            # print(temp)
            ans.append(temp)
        return ans