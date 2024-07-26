# Problem: C - InXtracting a Subsegment - https://codeforces.com/gym/537362/problem/C

a,b=(int(i) for i in input().split())
li=[int(i) for i in input().split()]

if b==1:
    print(min(li))
elif b==2:
    print(max(li[0],li[-1]))
else:
    print(max(li))