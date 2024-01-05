class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even=0
        ans=[]
        for i in nums:
            if i%2==0:
                even+=i
            
        for i in queries:
            if nums[i[1]] % 2==1:
                if i[0]%2==1:
                    even+=(i[0]+(nums[i[1]]))    
            else:
                if i[0]%2==1:
                    even-=nums[i[1]] 
                else:
                    even+= i[0]
            nums[i[1]]+=i[0]
            ans.append(even)

        return ans