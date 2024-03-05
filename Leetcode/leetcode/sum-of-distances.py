class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dic=defaultdict(list)
        ans=[0]*len(nums)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        print(dic)
        for key, value in dic.items():
            if len(value)==1:
                continue
            ps=[0]+value
            for i in range(1,len(value)+1):
                ps[i]=ps[i]+ps[i-1]
            print(ps)
            for i in range(len(value)):
                # print(value[i],ps[i])
                # print((i*value[i]-ps[i]))
                ans[value[i]]=(
                    (i*value[i]-ps[i])+
                    (ps[-1]-ps[i]- (value[i] * (len(value)-i)))
                )
            
        return ans
