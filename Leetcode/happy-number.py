class Solution:
    def isHappy(self, n: int) -> bool:
        general=set()

        while n!=1:
            if n in general:
                return False
            
            else:
                general.add(n)
                op=0
                x=str(n)
                for i in x:
                    op+=int(i)**2
                n=op

        return True
            
  