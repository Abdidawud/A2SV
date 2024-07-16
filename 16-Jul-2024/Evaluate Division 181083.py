# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        #   No division by zero
        adjacencyList = collections.defaultdict(list)   # A defaultdict is a dictionary-like object that automatically initializes values for nonexistent keys

        for i,eq in enumerate(equations):
            a,b = eq    # Each equation has two values
            adjacencyList[a].append([b,values[i]])  # Append [b,value(a/b)]
            adjacencyList[b].append([a,1/values[i]]) # b/a will be equal to 1 / (a/b)

        print(adjacencyList)
        def bfs(src,trg):
            if src not in adjacencyList or trg not in adjacencyList:
                return -1
            
            q = deque()
            visited = set()

            q.append([src,1])   # I'll append a node with the weight upto that node
            visited.add(src)
            
            while q:
                n , w = q.popleft() # Neighbor, Weight

                if n == trg:
                    return w

                for neighbor,weight in adjacencyList[n]:    # Iterating over the adjacency List of that particular node
                    if neighbor not in visited:
                        q.append([neighbor, w * weight])
                        visited.add(n)

            return -1

        return [bfs(query[0],query[1]) for query in queries]
    