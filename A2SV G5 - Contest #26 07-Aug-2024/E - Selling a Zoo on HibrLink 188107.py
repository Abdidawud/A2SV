# Problem: E - Selling a Zoo on HibrLink - https://codeforces.com/gym/537362/problem/E

import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    c = list(map(int, sys.stdin.readline().strip().split()))

    sons = [0] * n
    for i in range(n):
        a[i] -= 1
        sons[a[i]] += 1
        
    q = []
    for i in range(n):
        if sons[i] == 0:
            q.append(i)

    ans = []
    added = [0] * n
    while q:
        v = q.pop()
        ans.append(v)
        added[v] = 1
        sons[a[v]] -= 1
        if sons[a[v]] == 0:
            q.append(a[v])

    for v in range(n):
        if not added[v]:
            v2 = a[v]
            cycle = [v]
            while v2 != v:
                cycle.append(v2)
                v2 = a[v2]
            minc = 10 ** 9
            for u in cycle:
                added[u] = 1
                minc = min(minc, c[u])
            for i in range(len(cycle)):
                if c[cycle[i]] == minc:
                    ans += cycle[i + 1:]
                    ans += cycle[:i + 1]
                    break
    
    print(*map(lambda x: x + 1, ans))