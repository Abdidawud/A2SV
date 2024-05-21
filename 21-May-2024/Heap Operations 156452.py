# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

import heapq
n=int(input())
ans=[]
heap=[]

for _ in range(n):
    op=input().split()
    if op[0]=="insert":
        temp=int(op[1])
        heapq.heappush(heap,temp)
        ans.append((op[0],temp))
    
    elif op[0]=="removeMin":
        if not heap:
            ans.append(("insert",1))
        else:
            heapq.heappop(heap)
        ans.append((op[0],None))

    else:
        temp=int(op[1])
        while heap and heap[0]<temp:
            heapq.heappop(heap)
            ans.append(("removeMin",None))
        if not heap or heap[0]>temp:
            heapq.heappush(heap,temp)
            ans.append(("insert",temp))
        ans.append((op[0],temp))
# print(ans)
print(len(ans))
for i in ans:
    if i[1] is not None:
        print(i[0],i[1])
    else:
        print(i[0])
