class Solution:
    def isPalindrome(self, s: str) -> bool:
        li=[]
        for i in s:
            if ord(i)>=48 and ord(i)<=57:
                li.append(i)
            elif ord(i)>=65 and ord(i)<=90:
                li.append(i.lower())
            elif ord(i)>=97 and ord(i)<=122:
                li.append(i)
        
        st=''.join(li)
        st2=st[::-1]
        
        if st==st2:
            return True
        else:
            return False