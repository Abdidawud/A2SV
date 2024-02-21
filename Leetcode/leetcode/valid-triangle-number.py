class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans=0
        nums.sort()
        for i in range(2,len(nums)):
            j=0
            k=i-1
            temp=nums[i]
            while j<k:
                if nums[j]+nums[k]>temp:
                    ans+=k-j
                    k-=1
                else:
                    j+=1
        return ans