from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = {0: 0}
        for row in wall:
            total = 0
            for cell in row[:-1]:
                total += cell
                count[total] = 1 + count.get(total, 0)
        return len(wall) - max(count.values())
