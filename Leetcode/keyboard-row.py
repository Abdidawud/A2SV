class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row=[['Q','W','E','R','T','Y','U','I','O','P'],
            ['A','S','D','F','G','H','J','K','L'],
            ['Z','X','C','V','B','N','M']]

        ans=[]
        li=[]
        for i in range(len(words)):
            for j in range(3):
                x=words[i].upper()
                li=[char for char in x]
                set1=set(li)
                set2=set(row[j])
                
                if set1.issubset(set2):
                    ans.append(words[i])
                    li=[]
        
        return ans