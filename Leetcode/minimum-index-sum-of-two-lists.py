class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sum = len(list1) + len(list2)
        result = []
        for i in range(len(list1)):
            if list1[i] in list2:
                if i + list2.index(list1[i]) < index_sum:
                    index_sum = i + list2.index(list1[i])
                    result = [list1[i]]
                elif i + list2.index(list1[i]) == index_sum:
                    result.append(list1[i])
        return result
