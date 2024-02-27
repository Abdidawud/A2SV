class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans=[]
        all_chars=set()
        completed_chars=set()
        pointer=-1
        dic=Counter(s)
        for i in range(len(s)):
            all_chars.add(s[i])
            dic[s[i]]-=1

            if dic[s[i]]==0:
                completed_chars.add(s[i])
            
            if all_chars==completed_chars:
                ans.append(i-pointer)
                all_chars=set()
                completed_chars=set()
                pointer=i
        return ans