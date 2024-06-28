# Problem: D - The Equalizer XOR - https://codeforces.com/gym/528792/problem/D

import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    pref_xor = [a[0]]
    for i in range(1, n):
        pref_xor.append(pref_xor[-1] ^ a[i])
    yes = False
    if pref_xor[-1] == 0:
        yes = True
    for i in range(n):
        if yes:
            break
        first = pref_xor[i]
        for j in range(i + 1, n):
            second = pref_xor[j] ^ pref_xor[i]
            third = pref_xor[-1] ^ pref_xor[j]
            if first == second == third:
                yes = True
                break

    print('YES' if yes else 'NO')