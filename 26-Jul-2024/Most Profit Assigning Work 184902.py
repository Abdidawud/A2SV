# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        li=[]
        for i in range(len(profit)):
            li.append((difficulty[i],profit[i]))
        li.sort(key=lambda x: x[0])
        # print(li)
        max_profit=0
        for i in range(len(li)):
            if li[i][1]>max_profit:
                max_profit=li[i][1]
            li[i]=(li[i][0],max_profit)
        # print(li)
        def bs(arr,target):
            i=0
            j=len(arr)-1
            res=0
            while i<=j:
                mid=(i+j)//2
                if arr[mid][0]<= target:
                    res=arr[mid][1]
                    i=mid+1
                elif arr[mid][0]> target:
                    j=mid-1
            return res
        ans=0
        for i in worker:
            ans+=bs(li,i)
        return ans