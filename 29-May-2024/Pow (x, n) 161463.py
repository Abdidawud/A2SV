# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fun(base,pow):
            if pow==0:
                return 1
            if pow<0:
                return 1/fun(base,-pow)
            if pow%2==0:
                half= fun(base, pow//2)
                return half* half
            else:
                half=fun(base,pow//2)
                return half*half*base
        return fun(x,n)