class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backTrack(index, temp):
            if index == len(nums):
                ans.append(temp.copy())
                return
            else:
                temp.append(nums[index])
                backTrack(index + 1, temp)
                temp.pop()
                backTrack(index + 1, temp)

        backTrack(0, [])
        return ans