class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        one=[1]*numOnes
        zero=[0]*numZeros
        negOne=[-1]*numNegOnes
        li=[]
        li.extend(one)
        li.extend(zero)
        li.extend(negOne)
        ans=0
        for i in range(k):
            ans+=li[i]
        return ans