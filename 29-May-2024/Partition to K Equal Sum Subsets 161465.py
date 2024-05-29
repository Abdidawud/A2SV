# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        flag=[False]*len(nums)
        target=sum(nums)/k
        nums.sort(reverse=True)
        store={}

        def dp(i,k,sum_):
            if k==0:
                return True
            if sum_==target:
                return dp(0,k-1,0)
            if (tuple(flag),k,sum_) not in store:
                for j in range(i,len(nums)):
                    if flag[j] or sum_+nums[j] >target:
                        continue
                    flag[j]=True
                    if dp(j+1,k,sum_+nums[j]):
                        store[(tuple(flag),k,sum_)]=True
                        return True
                    flag[j]=False
                store[(tuple(flag),k,sum_)]=False
                return False
            return store[(tuple(flag),k,sum_)]
        return dp(0,k,0)