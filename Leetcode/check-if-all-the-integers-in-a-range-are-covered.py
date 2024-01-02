class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        li=[]
        ans=[]

        for i in range(left,right+1):
            li.append(i)
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                if j in li:
                    ans.append(j)
        set1=set(ans)
        set2=set(li)
        if not bool(set1):
            return False
        elif set2.issubset(set1):
            return True
        else:
            return False