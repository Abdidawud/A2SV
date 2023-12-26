class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x=len(indices)
        li=[0]*x
        for i in range(x):
            li[indices[i]]=s[i]
        return "".join(li)
        