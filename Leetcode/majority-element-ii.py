class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=math.floor(len(nums)/3)
        b=Counter(nums)
        ans=[]
        for i in b:
            if b[i]>a:
                ans.append(i)
        return ans