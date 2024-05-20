# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph=defaultdict(list)
        indegree=[len(i) for i in ingredients]

        for i in range(len(recipes)):
            for j in ingredients[i]:
                graph[j].append((recipes[i],i))
        # print(graph)
        # print(indegree)
        q=deque(supplies)
        ans=[]
        while q:
            temp=q.pop()
            for node in graph[temp]:
                indegree[node[1]]-=1
                if indegree[node[1]]==0:
                    ans.append(node[0])
                    q.append(node[0])
        return ans
