class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans=[]

        l=0
        r=1
        while r <(len(nums)-1):
            if nums[l]<(nums[r]+nums[(r+1)]):
                ans.append(nums[l]+nums[r]+nums[(r+1)])
                l+=1
                r+=1
            l+=1
            r+=1
        if len(ans)==0:
            return 0
        else:
            return (max(ans))
