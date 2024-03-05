class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(li,cur):
            if li==[]:
                ans.append(deepcopy(cur))
                return
            
            for i in range(len(li)):
                next_curr=cur+[li[i]]
                next_li=li[:i]+li[i+1:]
                backtrack(next_li,next_curr)
        backtrack(nums,[])
        return ans