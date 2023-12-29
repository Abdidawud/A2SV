class Solution:
    def reverseWords(self, s: str) -> str:
        li=s.split(" ")
        reve=li[::-1]
        ans=[]
        for i in reve:
            if i!="":
                ans.append(i)
        final=" ".join(ans)
        return final.strip()