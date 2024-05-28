# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children=[None]*2

class Solution:
    def __init__(self):
        self.root=TrieNode()
    def insert(self, num: str) -> None:
        cur=self.root
        bit=31
        while bit>=0:
            if num &(1<<bit):
                temp=1
            else:
                temp=0
            if not cur.children[temp]:
                cur.children[temp]=TrieNode()
                cur=cur.children[temp]
            else:
                cur=cur.children[temp]
            bit-=1
    def solve(self,num):
        res=0
        bit=31
        cur=self.root
        while bit>=0 and cur:
            if num &(1<<bit):
                temp=1
            else:
                temp=0
            
            if cur.children[(temp+1)%2]:
                cur=cur.children[(temp+1)%2]
                res+=(1<<bit)*((temp+1)%2)
            else:
                cur=cur.children[temp]
                res+=(1<<bit)*temp
            bit-=1
        return res

    def findMaximumXOR(self, nums: List[int]) -> int:
            for num in nums:
                self.insert(num)
            ans=0
            for num in nums:
                ans=max(ans,num^self.solve(num))
            return ans
        