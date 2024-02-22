class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        set_oper={'+','-','*','/'}
        ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y),"*": (lambda x,y: x*y),"/": (lambda x,y: x/y)}
        
        for i in tokens:
            if i in set_oper:
                y=int(stack.pop())
                x=int(stack.pop())
                stack.append(ops[i](x,y))
            else:
                stack.append(i)
        return int(stack[-1])