class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        li=[list(i) for i in zip(*strs)]
        ans=0
        for i in range(len(li)):
            for j in range(len(li[i])+1):
                if j==len(strs)-1:
                    break
                
                if ord(li[i][j+1])<ord(li[i][j]):
                    ans+=1
                    break
        
        return ans   