class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic1=defaultdict(int)
        dic2=defaultdict(int)
        ans=[]
        t=0

        for i in p:
            dic1[i]+=1
        for i in range(len(s)):
            if i<len(p):
                dic2[s[i]]+=1

            elif i>=len(p):
                dic2[s[i]]+=1
                dic2[s[t]]-=1
                if dic2[s[t]]<1:
                    dic2.pop(s[t])
                t+=1
            
            if dic1==dic2:
                ans.append(t)

        return ans