class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c=0
        common=[]
        not_common=[]
        sorter=set(arr2)
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j]==arr2[i]:
                    common.append(arr1[j])
                elif arr1[j] not in sorter and c==0:
                    not_common.append(arr1[j])
            c+=1
        not_common.sort()
        common.extend(not_common)
        

        return common