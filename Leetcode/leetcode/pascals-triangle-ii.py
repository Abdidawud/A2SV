class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[1]
        def rec_row(n,row):
            if n==0:
                return row
            next=[1]
            for i in range(len(row)-1):
                next.append(row[i]+row[i+1])
            next.append(1)
            return rec_row(n-1,next)
        return rec_row(rowIndex,ans) 