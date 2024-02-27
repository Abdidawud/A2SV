class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        stack=[]

        for num in reversed(nums2):
            while stack and stack[-1]< num:
                stack.pop()
            dic[num]=stack[-1] if stack else -1
            stack.append(num)
        ans=[dic[num]for num in nums1]
        return ans