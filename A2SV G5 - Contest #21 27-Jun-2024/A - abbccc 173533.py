# Problem: A - abbccc - https://codeforces.com/gym/530187/problem/A

n=int(input())
s=input()

i=0
j=1
ans=[]
while i<len(s):
    ans.append(s[i])
    i+=j
    j+=1
print(''.join(ans))