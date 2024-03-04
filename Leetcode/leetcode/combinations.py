class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        temp=[]
        def backtrack(j,current):
            
            if j==0:
                result.append(temp.copy())
                return
            for i in range(current,n+1):
                temp.append(i)
                backtrack(j-1,i+1)
                temp.pop()
        backtrack(k,1)
        return result
