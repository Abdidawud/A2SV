# Problem: Three sum - https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        my_set=set() 
        ans=[]

        for i in range(len(nums)-2):
            right=len(nums)-1
            left=i+1
            while left<right:
                
                if nums[i]+nums[left]+nums[right]==0:
                    x=(nums[i],nums[left],nums[right])
                    my_set.add(x)
                    left+=1
                elif nums[i]+nums[left]+nums[right]>0:
                    right-=1
                else:
                    left+=1

        for i in my_set:
            ans.append(list(i))
        
        return ans