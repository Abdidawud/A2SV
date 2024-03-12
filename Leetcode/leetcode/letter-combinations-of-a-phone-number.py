class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping={
                "2":"abc",
                "3":"def",
                "4":"ghi",
                "5":"jkl",
                "6":"mno",
                "7":"pqrs",
                "8":"tuv",
                "9":"wxyz"
        }
        ans=[]

        def backtrack(i,temp):
            if len(temp)==len(digits):
                ans.append(temp)
                return
            
            for char in mapping[digits[i]]:
                backtrack(i+1,temp+char)
        
        if digits:
            backtrack(0,"")
        return ans
            