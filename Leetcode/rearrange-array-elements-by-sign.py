class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        ans=[]
        for i in range(len(nums)):
            if nums[i]>0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        for i in range(len(nums)//2):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans
        