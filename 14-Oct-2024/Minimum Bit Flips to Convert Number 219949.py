# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        temp=start^goal
        bit=bin(temp)
        ans=0
        for i in range(2,len(bit)):
            if bit[i]=='1':
                ans+=1
        return ans