class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        i=0
        j=1

        while i!=len(nums)-1:
            if nums[i]+nums[j]==target:
                ans.append(i)
                ans.append(j)
                break
            elif j==len(nums)-1:
                i+=1
                j=i+1
            else:
                j+=1
        
        return ans