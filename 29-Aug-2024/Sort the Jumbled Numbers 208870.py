# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def helper(n):
            x=list(str(n))
            for i in range(len(x)):
                x[i]=str(mapping[int(x[i])])
            return int("".join(x))
        
        ans=sorted(nums,key=lambda x:helper(x))
        return ans