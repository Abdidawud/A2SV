class Solution:
    def totalMoney(self, n: int) -> int:
        ans=0
        total=0
        for i in range(n):
            if i%7==0:
                ans=i//7 + 1
            else:
                ans+=1
            total+=ans
        return total