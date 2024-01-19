class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        first=0
        second=0

        while second < len(typed):
        
            if first<len(name) and name[first] == typed[second]:
                first+=1
                second+=1
            elif second>0 and typed[second-1]== typed[second]:
                second+=1
            else:
                return False
                break
        
        return first ==len(name)
            