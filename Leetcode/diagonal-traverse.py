class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        dic=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dic[i+j].append(mat[i][j])

        solution=[]
        for i in dic:
            if i%2==0:
                solution+=(dic[i][::-1])
            else:
                solution+=(dic[i])
        
        return solution