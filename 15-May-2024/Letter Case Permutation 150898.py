# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=[]
        def backtrack(i,cur):
            if i== len(s):
                ans.append(cur)
                return 
            if s[i].isalpha():
                backtrack(i+1,cur+s[i].upper())
                backtrack(i+1,cur+s[i].lower())
            else:
                backtrack(i+1,cur+s[i])
        backtrack(0,"")
        return ans