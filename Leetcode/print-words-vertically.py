class Solution:
    def printVertically(self, s: str) -> List[str]:
        y=s.split()
        maxx=0
        l=[]
        for _ in y:
            maxx=max(maxx,len(_))
        for i in range(maxx):
            ans=""
            for j in range(len(y)):
                if i>=len(y[j]):
                    ans+=" "
                else:
                    ans+=(y[j][i])
            l.append(ans.rstrip())
        return l