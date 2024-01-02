class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]

        for i in range(len(boxes)):
            op=0
            for j in range(len(boxes)):
                if boxes[j]=='1':
                    op+=abs(j-i)
            ans.append(op)    
        
        return ans