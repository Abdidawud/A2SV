class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        left=0
        right=1
        answer=[]
        while right<=len(nums)-1:
            i=nums[left]
            for _ in range(i):
                answer.append(nums[right])
            right+=2
            left+=2
        return answer