# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # i=0
        # ans=0
        # while i< len(arrays):
        #     j=0
        #     while j <len(arrays):
        #         if i!=j:
        #             temp=arrays[i][-1]-arrays[j][0]
        #             if ans<temp:
        #                 ans=temp
        #         j+=1
        #     i+=1
        # return ans

        max_=arrays[0][-1]
        min_=arrays[0][0]
        ans=0

        for i in range(1,len(arrays)):
            temp1=abs(arrays[i][0]-max_)
            temp2=abs(arrays[i][-1]-min_)
            ans=max(ans,temp1,temp2)
            max_=max(arrays[i][-1],max_)
            min_=min(arrays[i][0],min_)
        return ans