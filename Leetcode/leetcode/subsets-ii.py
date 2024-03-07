class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()

        def backtrack(index,subset):
            if index==len(nums):
                ans.append(subset.copy())
                return
            
            subset.append(nums[index])
            backtrack(index+1,subset)
            subset.pop()

            while index+1 <len(nums) and nums[index]==nums[index+1]:
                index+=1
            backtrack(index+1,subset)
        backtrack(0,[])
        return ans