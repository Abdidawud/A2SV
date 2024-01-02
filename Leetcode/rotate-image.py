class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        img=[]
        matrix.reverse()
        for i in range(len(matrix)):
            lst = []
            for j in range(len(matrix)):
                lst.append(matrix[j][i])
            img.append(lst)
        for i in range(len(img)):
            for j in range(len(img)):
                matrix[i][j] = img[i][j]
    