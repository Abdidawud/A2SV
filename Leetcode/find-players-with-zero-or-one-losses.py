class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners=dict(Counter([i[0] for i in matches]).items())
        loosers=dict(Counter([i[1] for i in matches]).items())
        nolose=[]
        onelose=[]
        ans=[]
        for i in winners:
            if i not in loosers:
                nolose.append(i)

        for i in loosers:
            if loosers[i]==1:
                onelose.append(i)
        nolose.sort()
        onelose.sort()

        ans.append(nolose)
        ans.append(onelose)
        
        return ans