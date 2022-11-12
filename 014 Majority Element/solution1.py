from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_elements = defaultdict(int)
        for num in nums:
            count_elements[num] += 1
        return max(count_elements, key=count_elements.get)
