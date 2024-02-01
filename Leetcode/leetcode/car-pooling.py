class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_=0
        for i in trips:
            max_=max(max_,i[2])
        ps=[0]*(max_+1)
        for i,j,k in trips:
            ps[j]+=i
            ps[k]-=i
        sum=0
        for i in range(len(ps)):
            sum+=ps[i]
            ps[i]=sum
        
        for i in ps:
            if i>capacity:
                return False
        return True
            