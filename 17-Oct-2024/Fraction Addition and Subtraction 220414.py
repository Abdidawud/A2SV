# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:
        stack = []
        i = 0
        temp = ""
        while i < len(expression):
            if i == 0 and expression[i] == "-":
                temp +="-"
            else:
                j = 0
                ind = 0
                while i < len(expression) and (expression[i] != "-" and expression[i] != "+"):
                    temp +=expression[i]
                    j +=1
                    if expression[i] == "/":
                        ind = j
                    i +=1
                stack.append((temp,ind))
                if i < len(expression) and expression[i] == "-":
                    temp = "-"
                else:
                    temp = ""
            i +=1
        ans = []
        for ch,i in stack:
            if ch[0] == "-":
                ans.append([-int(ch[1:i]),int(ch[i+1:])])
            else:
                ans.append([int(ch[:i-1]),int(ch[i:])])

        numerator = 0
        denominator = 1
        for nm,dn in ans:    
            denominator *=dn
        for nm,dn in ans:
            numerator += nm * (denominator // dn)

        gcd = math.gcd(numerator, denominator)
    
        numerator = numerator // gcd
        denominator = denominator // gcd

        return f'{numerator}/{denominator}'