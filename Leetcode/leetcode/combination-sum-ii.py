class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        
        def backtrack(combination,pos,target):
            if target==0:
                ans.append(combination.copy())
            if target <0:
                return
            
            prev=-1
            for i in range(pos,len(candidates)):
                if candidates[i]==prev:
                    continue
                combination.append(candidates[i])
                backtrack(combination,i+1,target-candidates[i])
                combination.pop()
                prev=candidates[i]
        backtrack([],0,target)
        return ans
