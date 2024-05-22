# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispal(k,i,j):
            while i<j:
                if k[i]!=k[j]:
                    return False
                i+=1
                j-=1
            return True
        
        ans=[]
        cur=[]
        def backtrack(i):
            if i>=len(s):
                ans.append(cur.copy())
                return 
            for j in range(i,len(s)):
                if ispal(s,i,j):
                    cur.append(s[i:j+1])
                    backtrack(j+1)
                    cur.pop()
        backtrack(0)
        return ans