class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        dic=defaultdict(list)
        for x,y in points:
            temp=0
            temp=(x**2)+(y**2)
            dic[temp].append([x,y])
      
        sorted_dic={x:dic[x] for x in sorted(dic)}
      

        for i in sorted_dic.keys():
            count=0
            while count<len(sorted_dic[i]) and len(ans)<k:
                ans.append(sorted_dic[i][count])
                count+=1
        return ans