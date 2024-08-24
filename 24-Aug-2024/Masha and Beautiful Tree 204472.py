# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

def func(n):
    ele = -1
    arr = []
    for i in range(n):
        ele += 2
        arr.append(ele)
    
    print(" ".join(map(str, arr)))

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        func(n)

if __name__ == "__main__":
    main()
