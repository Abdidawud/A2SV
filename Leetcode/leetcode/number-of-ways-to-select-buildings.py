class Solution:
    def numberOfWays(self, s: str) -> int:
        dict_=defaultdict(int)
        for i in range(len(s)-1,-1,-1):
            if s[i]=="1":
                dict_['1']+=1
                dict_['10'] +=dict_['0']
                dict_['101'] +=dict_['01']
            else:
                dict_['0']+=1
                dict_['01']+=dict_['1']
                dict_['010']+=dict_['10']
        
        return (dict_['010']+dict_['101'])