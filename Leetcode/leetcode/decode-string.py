class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i!=']':
                stack.append(i)
            else:
                char=''
                while stack and stack[-1]!='[':
                    char=stack.pop()+  char
                stack.pop()
                number=''
                while stack and stack[-1].isdigit():
                    number=stack.pop()+number
                char*=int(number)
                stack.append(char)
        return "".join(stack)