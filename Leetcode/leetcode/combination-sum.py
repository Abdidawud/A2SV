class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def backtrack(index,combination,total):
            if total==target:
                ans.append(combination.copy())
                return
            if index >= len(candidates) or total > target:
                return
            
            combination.append(candidates[index])
            backtrack(index,combination,total+candidates[index])
            combination.pop()
            backtrack(index+1,combination,total)

        backtrack(0,[],0)
        return ans