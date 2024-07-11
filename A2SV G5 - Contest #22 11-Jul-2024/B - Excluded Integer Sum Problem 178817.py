# Problem: B - Excluded Integer Sum Problem - https://codeforces.com/gym/531455/problem/B

def solve():
    n, k, x = map(int, input().split())

    if x != 1:
        print("YES")
        print(n)
        print("1 " * n)
    else:
        if k >= 2 and n % 2 == 0:
            print("YES")
            print(n // 2)
            print("2 " * (n // 2))
        elif k >= 3:
            print("YES")
            print(n // 2, "3", end=" ")
            print("2 " * (n // 2 - 1))
        else:
            print("NO")

if __name__ == "__main__":
    T = 1
    T = int(input())
    for _ in range(T):
        solve()