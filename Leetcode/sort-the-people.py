class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic={}
        for i in range(len(names)):
            dic[heights[i]]=names[i]
        print(dic)
        sorted_dict = dict(sorted(dic.items(), reverse=True))
        ans=[]

        for i in sorted_dict.values():
            ans.append(i)

        return ans