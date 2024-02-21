class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic=defaultdict(int)
        ans=0

        for i in range(len(answers)):
            if answers[i]==0:
                ans+=1
            else:
                if dic[answers[i]]>0:
                    dic[answers[i]]-=1
                else:
                    ans+=answers[i]+1
                    dic[answers[i]]+=answers[i]
        return ans
        