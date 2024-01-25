class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=[]
        dic=defaultdict(int)

        for i in range(len(nums)-2):
            right=len(nums)-1
            left=i+1

            while left<right:
                x=0
                x=nums[i]+nums[left]+nums[right]
                dic[x]=abs(x-target)
                if x>target:
                    right-=1
                else:
                    left+=1

        dic=dict(sorted(dic.items(),key=lambda item :item[1]))
        for i in dic:
            return i