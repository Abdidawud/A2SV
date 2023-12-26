class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        li1=nums[:n]
        li2=nums[n:]
        ans=[]
        for i in range(n):
            ans.append(li1[i])
            ans.append(li2[i])
        return ans
        