# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_no=(2**maximumBit)-1
        ans=[]
        # while len(nums)>0:
        #     temp=nums[0]
        #     for i in range(1,len(nums)):
        #         temp^=nums[i]
        #     temp^=max_no
        #     ans.append(temp)
        #     nums.pop()
        # return ans

        xor=[]
        temp=0
        for i in range(len(nums)):
            temp^=nums[i]
            xor.append(temp)
        while xor:
            t=xor.pop()
            ans.append(t^max_no)
        return ans
