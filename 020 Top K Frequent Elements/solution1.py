from collections import Counter
from typing import List


class Solution:
    def topKFrequent(
        self,
        nums: List[int],
        k: int
    ) -> List[int]:
        nums_counter = Counter(nums).most_common(k)
        return list(
            map(lambda x: x[0], nums_counter)
        )
