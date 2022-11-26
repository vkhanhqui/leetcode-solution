from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = defaultdict(int)
        count.update({0: 0})
        for row in wall:
            total = 0
            for cell in row[:-1]:
                total += cell
                count[total] += 1
        return len(wall) - max(count.values())
