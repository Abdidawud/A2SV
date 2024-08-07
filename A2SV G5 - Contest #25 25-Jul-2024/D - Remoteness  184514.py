# Problem: D - Remoteness  - https://codeforces.com/gym/535749/problem/D

import sys
import math
 
n=int(input())
e=[[] for _ in range(n)]
for _ in range(n):
   x,y=map(int,input().split())
   e[x-1].append(y-1)
   e[y-1].append(x-1)
d=[len(x) for x in e]
q=[i for i in range(n) if d[i]==1]
 
c=[0]*n
for u in q:
   c[u]=n
   for v in e[u]:
        d[v]-=1
        if d[v]==1:
            q.append(v)
q.extend(i for i in range(n) if not c[i])
for u in q[::-1]:
   for v in e[u]:
   	c[v]=min(c[v],c[u]+1)
print(" ".join(map(str,c)))