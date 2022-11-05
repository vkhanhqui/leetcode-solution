from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sub_rs = {}
        for _str in strs:
            new_str = ''.join(sorted(list(_str)))
            if new_str in sub_rs:
                sub_rs[new_str].append(_str)
            else:
                sub_rs[new_str] = []
                sub_rs[new_str].append(_str)
        return list(sub_rs.values())
