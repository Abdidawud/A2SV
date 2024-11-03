# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        greater=[]
        piv=[]
        ans=[]
        for i in nums:
            if i>pivot:
                greater.append(i)
            elif i<pivot:
                less.append(i)
            elif i==pivot:
                piv.append(i)
        ans=less+piv+greater

        return ans
            