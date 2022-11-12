from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_nums = Counter(nums).items()
        thredsold = len(nums)/2
        for k, v in count_nums:
            if v > thredsold:
                return k
