class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ans=[]

        for i in range(len(words)):
            li=[]
            for j in range (len(words[i])):
                li.append(order.index(words[i][j]))
            ans.append(li)


        if(ans== sorted(ans)):
            return True
        else:
            return False
