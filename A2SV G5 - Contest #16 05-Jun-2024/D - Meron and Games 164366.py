# Problem: D - Meron and Games - https://codeforces.com/gym/523525/problem/D

import sys, threading
from collections import *
input = lambda: sys.stdin.readline().strip()

def main():
    store={}
    n=int(input())
    li=[int(i) for i in input().split()]
    count=Counter(li)
    max_=max(li)
    def dp(num):
        if num>max_:
            return 0
        if num not in store:
            store[num]=max((count[num]*num)+dp(num+2),dp(num+1))
        return store[num]
    print(dp(1))
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
