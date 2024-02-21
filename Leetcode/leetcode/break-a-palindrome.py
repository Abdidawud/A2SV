class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)<=1:
            return ""
        li=list(palindrome) 
       
        for i in range(len(li)):
            if i==len(li)-1:
                li[i]="b"
            elif li[i] !='a' and li.count(li[i])>1:
                li[i] = 'a'
                break
        
                 
        return (''.join(li))