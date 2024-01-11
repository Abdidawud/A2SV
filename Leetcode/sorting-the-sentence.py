class Solution:
    def sortSentence(self, s: str) -> str:
        li=s.split()
        li.sort(key=lambda j:j[-1])
        ans=[]
        
        for i in li:
            ans.append(i[:-1])
        
        return (" ".join(ans))