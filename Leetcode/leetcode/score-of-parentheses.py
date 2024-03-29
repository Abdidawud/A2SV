class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        dic=defaultdict(int)
        for i in s:
            if i=='(':
                stack.append(0)
                
            else:
                top=stack.pop()
                val=max(1,2*top)
                stack[-1]+=val
        
        return(stack.pop())