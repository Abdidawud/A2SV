# Problem: B - Instructions - https://codeforces.com/gym/523525/problem/B

import sys, threading
input = lambda: sys.stdin.readline().strip()

def main():
    t=int(input())
    for _ in range(t):
        n=int(input())
        li=[int(i) for i in input().split()]
        ans=0
        store={}
        def dp(i):
            nonlocal ans
            if i>=n:
                return 0
            if i in store:
                return store[i]
            store[i]=li[i]+dp(li[i]+i)
            return store[i]
        for j in range(n):
            dp(j)

        print (max(store.values()))

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
