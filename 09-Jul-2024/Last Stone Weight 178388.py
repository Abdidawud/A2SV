# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        while len(stones)>1:
            heapify(stones)
            x=heappop(stones)
            y=heappop(stones)

            if x==y:
                continue
            if x<y:
                temp=x-y
            else:
                temp=y-x
            heappush(stones,temp)
        if stones:
            return -1 *stones[0]
        else:
            return 0

