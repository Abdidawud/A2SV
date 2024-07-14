# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        li1=[]
        li2=[]
        for i in s:
            if i != '#':
                li1.append(i)
            elif li1 and i=="#":
                li1.pop()
        for i in t:
            if i != '#':
                li2.append(i)
            elif li2 and i=="#":
                li2.pop()
        
        if li1==li2:
            return True
        return False