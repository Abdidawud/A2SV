# Problem: B - BANless - https://codeforces.com/gym/528792/problem/B

for _ in range(int(input())):
    n = int(input())
    li= []
    
    start, end = 1, 3 * n 
    while start < end:
        li.append([start, end])
        start += 3
        end -= 3    

    print(len(li))
    for i in li:
        print(*i) 
    