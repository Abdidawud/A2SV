class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        li=list(s)
        arr1=[0]*len(s)
        arr2=[0]*len(s)

        for i, j, k in shifts:
            if k==0:
                arr2[i]+=1
                if j+1<len(s):
                    arr2[j+1]-= 1
            else:
                arr1[i]+=1
                if j+1<len(s):
                    arr1[j+1]-=1
        prefix_sum=0
        postfix_sum=0

        for i in range(len(s)):
            prefix_sum+=arr1[i]
            postfix_sum+=arr2[i]

            shift=prefix_sum-postfix_sum

            char=ord(li[i])
            char=(char-97+shift)%26+97
            li[i]=chr(char)

        return (''.join(li))