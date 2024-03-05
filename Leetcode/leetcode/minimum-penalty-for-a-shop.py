class Solution:
    def bestClosingTime(self, s: str) -> int:
        prefix_countN=[0]
        suffix_countY=[]

        count_N=0
        for char in s:
            if char=='N':
                count_N+=1
            prefix_countN.append(count_N)
        count_Y=0
        for char in reversed(s):
            if char=='Y':
                count_Y+=1
            suffix_countY.insert(0,count_Y)
        suffix_countY.append(0)
        i=0
        while i <len(prefix_countN):
            prefix_countN[i]=prefix_countN[i]+suffix_countY[i]
            i+=1
        min_=float('inf')
        index=float('inf')
        for i in range(len(prefix_countN)):
            if prefix_countN[i] < min_:
                min_=prefix_countN[i]
                index=i
                
        return index
        