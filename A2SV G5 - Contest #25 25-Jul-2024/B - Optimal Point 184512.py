# Problem: B - Optimal Point - https://codeforces.com/gym/535749/problem/B

t = int(input())
for _ in range(t):
    N, K = map(int, input().split())
    l_ = r_ = False
    for _ in range(N):
        l, r = map(int, input().split())   
        if l == K:
            l_ = True
        if r == K:
            r_ = True
    
    if l_ and r_:
        print("YES")
    else:
        print("NO")