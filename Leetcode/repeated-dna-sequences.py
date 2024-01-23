class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 0
        dic =  defaultdict(int)
        for R in range(9, len(s)):
            dic[s[L:R+1]]+=1
            L+=1
        ans = []
        for chrs in dic:
            if dic[chrs]>1:
                ans.append(chrs)
        return ans