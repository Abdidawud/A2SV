class Solution:
    def largestOddNumber(self, num: str) -> str:
        li=num[::-1]
        ans=""
        for i in range(len(li)):
            if int(li[i])%2!=0:
                ans+=li[i:]
                break
            else:
                i+=1
        ans=ans[::-1]
        return ans
                