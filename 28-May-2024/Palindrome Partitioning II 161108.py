# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        def ispal(k,i,j):
            while i<j:
                if k[i]!=k[j]:
                    return False
                i+=1
                j+=1
            return True
        
        store={}
        def dp(i):
            if i>=len(s):
                return 0
            if i in store:
                return store[i]
            ans=float("inf")
            for j in range(i,len(s)+1):
                if s[i:j+1]==s[i:j+1][::-1]:
                    ans=min(ans,1+dp(j+1))
            store[i]=ans if ans != float("inf") else 0
            return store[i]
        return dp(0)-1