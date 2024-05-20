# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dir=[(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0)
            ,(0,0,0,-1),(0,0,-1,0),(0,-1,0,0),(-1,0,0,0)]

        initial=[0,0,0,0,0]
        li=[int(i) for i in target]
        # print(li)
        dead=set(deadends)
        if '0000' in dead:
            return -1
        q=deque([initial])
        visited=set()
        visited.add((0,0,0,0))

        while q:
            bound=len(q)
            for _ in range(bound):
                a,b,c,d,dis=q.popleft()
                # print(dis)
                if [a,b,c,d]==li:
                    return dis
                for e,f,g,h in dir:
                    i=(a-e+10)%10
                    j=(b-f+10)%10
                    k=(c-g+10)%10
                    l=(d-h+10)%10
                    if f"{i}{j}{k}{l}" not in dead:
                        if (i,j,k,l) not in visited:
                            visited.add((i,j,k,l))
                            q.append([i,j,k,l,dis+1])
        return -1
