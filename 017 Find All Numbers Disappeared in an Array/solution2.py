from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        return [
            index
            for index in range(1, len(nums) + 1)
            if index not in set_nums
        ]
