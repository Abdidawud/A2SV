
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_index_map = {num: index for index, num in enumerate(nums)}
        
        for operation in operations:
            num, new_value = operation
            if num in num_index_map:
                index = num_index_map[num]
                nums[index] = new_value
                del num_index_map[num]
                num_index_map[new_value] = index
        
        return nums
