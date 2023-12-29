class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic=Counter(arr)
        for i in dic:
            if dic[i] > len(arr)//4:
                return i
                break