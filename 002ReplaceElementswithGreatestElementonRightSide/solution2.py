from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r_index = len(arr) - 1
        r_max = -1
        while r_index > -1:
            current_value = arr[r_index]
            arr[r_index] = r_max
            if current_value > r_max:
                r_max = current_value
            r_index -= 1
        return arr
