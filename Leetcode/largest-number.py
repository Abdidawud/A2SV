class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=lambda x:str(x)*10, reverse=True)
        s=''.join(str(i) for i in nums)

        if int(s[0])==0:
            return "0"
        return s