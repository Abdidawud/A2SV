class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')':'(','}':'{',']':'['}
        
        for i in s:
            if len(stack)<1 or i not in dic:
                stack.append(i)
            elif dic[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        if stack:
            return False
        
        return True
