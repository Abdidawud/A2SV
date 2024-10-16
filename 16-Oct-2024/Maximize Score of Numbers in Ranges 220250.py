# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        def helper(mid):
            last=-float('inf')
            for i in start:
                if last +mid>i+d:
                    return False
                last=max(i,last+mid)
            return True
        start.sort()
        l=0
        r=start[-1]+d-start[0]
        while l<r:
            mid=(l+r+1)//2
            if helper(mid):
                l=mid
            else:
                r=mid-1
        return l