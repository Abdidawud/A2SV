# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets=set([0,firstPerson])
        parent={}

        for src,des,time in meetings:
            if time not in parent:
                parent[time]=defaultdict(list)
            parent[time][src].append(des)
            parent[time][des].append(src)
        # print(parent)
        

        def dfs(src,adj):
            if src in visited:
                return 
            visited.add(src)
            secrets.add(src)
            for neighbour in adj[src]:
                dfs(neighbour,adj)
        
        for t in sorted(parent.keys()):
            visited=set()
            for src in parent[t]:
                if src in secrets:
                    dfs(src,parent[t])
        return list(secrets)