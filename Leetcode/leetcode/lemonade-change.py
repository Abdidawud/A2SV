class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic=defaultdict(int)
        for i in bills:
            if i==5:
                dic[i]+=1
            elif i==10:
                dic[i]+=1
                if dic[5]>=1:
                    dic[5]-=1
                
                else:
                    return False
            elif i==20:
                if dic[5]>=1 and dic[10]>=1:
                    dic[5]-=1
                    dic[10]-=1
                elif dic[5]>=3:
                    dic[5]-=3
                else:
                    return False
        return True
            