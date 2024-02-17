class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr=[0]*(len(nums)+1)
        for i,j in requests:
            arr[i] +=1
            arr[j+1] -=1
        for i in range(1,len(arr)):
            arr[i]+=arr[i-1]
        
        nums.sort(reverse=True)
        arr.sort(reverse=True)

        ans=0
        for i in range(len(nums)):
            ans+=nums[i]*arr[i]
        return ans % (10**9+7)