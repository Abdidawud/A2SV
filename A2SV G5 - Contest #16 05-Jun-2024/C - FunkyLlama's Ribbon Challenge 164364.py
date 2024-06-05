# Problem: C - FunkyLlama's Ribbon Challenge - https://codeforces.com/gym/523525/problem/C

import sys, threading
input = lambda: sys.stdin.readline().strip()

def main():
    n,a,b,c=(int(i) for i in input().split())
    store={}
    def dp(n):
        if n==0:
            return 0
        if n<0:
            return -1000000000
        if n not in store:
            store[n]=max(dp(n-a)+1,dp(n-b)+1,dp(n-c)+1)
        return store[n]
    print (dp(n))
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
