from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sub_rs = defaultdict(list)
        for _str in strs:
            sub_rs[tuple(sorted(_str))].append(_str)
        return list(sub_rs.values())
