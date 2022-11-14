from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        len_num = len(nums)
        one_to_n = [i for i in range(1, len_num+1)]
        rs = []
        for num in one_to_n:
            if num not in nums:
                rs.append(num)
        return rs
