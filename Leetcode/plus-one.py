class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strs=''
        for i in digits:
            strs+=str(i)
        integer=int(strs)+1
        x=str(integer)
        ans=[]
        for i in x:
            ans.append(int(i))

        return ans