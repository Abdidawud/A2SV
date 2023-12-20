class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        z=y[::-1]
        if z[-1]=="-":
            return False
        else:
            a=int(z)

        if a==x:
            return True
        else:
            return False