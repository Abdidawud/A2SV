class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        i=0
        j=1
        li=[]
        while j <len(weights):
            temp=weights[i]+weights[j]
            li.append(temp)
            i+=1
            j+=1
        li.sort()
        left=0
        right=len(weights)-1
        left_sum=sum(li[0:left+(k-1)])
        right_sum=sum(li[right-(k-1):right+1])
        return (right_sum-left_sum)