# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not set(words[i]).intersection(set(words[j])):
                    temp=len(words[i])*len(words[j])
                    ans=max(ans,temp)
        return ans