class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count={}
        result=0
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        
        for num in count.values():
            result +=num *(num-1)//2
        
        return result