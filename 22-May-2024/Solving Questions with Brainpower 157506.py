# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        store={}
        def dp(i):
            if i >=len(questions):
                return 0
            if i not in store:
                one=questions[i][0]+dp(i+questions[i][1]+1)
                two=dp(i+1)
                store[i]=max(one,two)
            return store[i]
        return dp(0)
