class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        li=[i for i in path.split('/') if i]
        print(li)
        for i in li:
            if i=='..':
                if stack:
                    stack.pop()
                continue
            if i=='.':
                continue
            stack.append(i)
        return '/'+'/'.join(stack)
