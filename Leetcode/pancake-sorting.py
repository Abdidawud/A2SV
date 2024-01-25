class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]

        while len(arr)>1:
            maxx=max(arr)
            ind=arr.index(maxx)+1
            li=list(reversed(arr[:ind]))
            li=li+arr[ind:]
            arr=li
            ans.append(ind)
            arr.reverse()
            ans.append(len(arr))
            arr.pop()
        
        return ans