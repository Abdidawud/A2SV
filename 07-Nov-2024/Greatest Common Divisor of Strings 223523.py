# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_=gcd(len(str1),len(str2))
        ans=str1[:gcd_]
        temp1=len(str1)//len(ans)
        temp2=len(str2)//len(ans)

        if ans *temp1 == str1 and ans *temp2== str2:
            return ans
        return ''