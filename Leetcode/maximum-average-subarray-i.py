class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=0
        li=[]
        for i in range(k):
            s += nums[i]
        av=s/k
        li.append(s)

        for i in range(1,len(nums)- k+1):
            s=s-nums[i-1] + nums[k+i-1]
            if s/k>av:
                av=s/k
        return (float("{:.5f}".format(av)))