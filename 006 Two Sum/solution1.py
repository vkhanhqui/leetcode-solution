from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        len_nums = len(nums)
        first_value = nums[0]
        index = 1
        reset_index = 1
        flag = True
        while flag:
            if (
                first_value + nums[index] == target and
                index != reset_index - 1
            ):
                result = [reset_index-1, index]
                flag = False
            index += 1
            if index == len_nums:
                index = reset_index
                reset_index += 1
                first_value = nums[index]
        return result
