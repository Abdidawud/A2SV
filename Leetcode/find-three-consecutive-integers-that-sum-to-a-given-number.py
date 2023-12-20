class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        l=[]
        x=num//3
        y=x+1
        z=x-1

        sum=x+y+z

        if sum==num:
            l.append(z)
            l.append(x)
            l.append(y)

            return l
        else:
            return []
       
                
          
                 