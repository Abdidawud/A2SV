# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        dic={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,
        'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

        ans=''
        for i in s:
            ans+=str(dic[i])
        
        while k>0:
            temp=0
            for i in range(len(ans)):
                temp+=int(ans[i])
            ans=str(temp)
            k-=1
        return int(ans)
