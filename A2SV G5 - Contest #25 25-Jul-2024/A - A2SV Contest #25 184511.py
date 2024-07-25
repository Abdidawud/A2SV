# Problem: A - A2SV Contest #25 - https://codeforces.com/gym/535749/problem/A

import sys
input = lambda: sys.stdin.readline().rstrip()
a, b, c, d = map(int, input().split())
def find_points(p, t):
    return max((3*p)//10, p - (p*t)//250)
m = find_points(a, c)
v = find_points(b, d)

if m > v:
    print('Misha')
elif m < v:
    print('Vasya')
else:
    print('Tie')