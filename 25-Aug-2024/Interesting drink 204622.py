# Problem: Interesting drink - https://codeforces.com/problemset/problem/706/B/

from bisect import bisect_right

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    
    a.sort()
    
    for _ in range(m):
        k = int(input())
        ans = bisect_right(a, k)
        print(ans)

if __name__ == "__main__":
    main()
