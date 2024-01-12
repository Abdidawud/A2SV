class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_=max(arr)
        x=arr.index(max_)

        flag=False
        count=0
        if x==0 or x==(len(arr)-1):
            return False

        for i in range(len(arr)-1):
            if arr[i+1]>arr[i] and not flag:
                count+=1
            elif arr[i]>arr[i+1]:
                flag=True
            else:
                return False

        return True