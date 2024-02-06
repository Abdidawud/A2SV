class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        dic=defaultdict(int)
     
        for i in range(k):
            dic[blocks[i]]+=1
        min_=dic['W']

        for i in range(k,len(blocks)):
            dic[blocks[i]]+=1
            dic[blocks[i-k]]-=1
            min_=min(min_,dic['W'])
        return min_