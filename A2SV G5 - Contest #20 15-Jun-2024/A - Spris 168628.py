# Problem: A - Spris - https://codeforces.com/gym/528792/problem/A

a = int(input())
b = int(input())
c = int(input())

temp=min(a // 1, b // 2, c // 4)
ans=temp*7
print(ans)
