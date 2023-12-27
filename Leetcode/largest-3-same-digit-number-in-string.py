class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l=list(num)
        ans=[]
        z=''
        for i in range(len(l)-2):
            if i==l[-3]:
                if l[i]==l[i+1]:
                    return ""
                    break
            else:
                if l[i]==l[i+1] and l[i]==l[i+2]:
                    ans+=(l[i])
                
                    y=max(ans)
                
                    z=(y+y+y)
        return (z)