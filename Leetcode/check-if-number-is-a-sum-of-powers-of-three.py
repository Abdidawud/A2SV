class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        m=n
        sum=0
        l=[]
        while n!=0:
            l.append(n%3)
            n=n//3
        for i in range (len(l)):
            if l[i]==0:
                continue
            sum+=(3**i)
        
        if m==sum:
            return True
        else:
            return False