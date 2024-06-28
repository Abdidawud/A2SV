# Problem: B - Distinct Digits - https://codeforces.com/gym/530187/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    for i in range(9, 0, -1):
        if n >= i:
            ans.append(i)
            n -= i
    ans.reverse()
    print(*ans, sep="")