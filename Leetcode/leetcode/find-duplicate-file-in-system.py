class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in paths:
            List=i.split()
            root=List[0]
            for j in List[1:]:
                temp=j.split('(')
                name=temp[0]
                value=temp[1]
                dic[value].append(f"{root}/{name}")
        ans=[]
        for i in dic:
            if len(dic[i])>1:
                ans.append(dic[i])
        return ans