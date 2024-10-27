# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

from heapq import heapify
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ls = [-i for i in nums]
        heapify(ls)
        summ = 0
        for i in range(k):
            k = heappop(ls)
            summ+=(-k)
            heappush(ls,k-1)
        return summ

