# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=math.floor(len(nums)/3)
        b=Counter(nums)
        ans=[]
        for i in b:
            if b[i]>a:
                ans.append(i)
        return ans