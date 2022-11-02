from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_cp = arr.copy()
        len_arr = len(arr)
        index = 0
        while index < len_arr:
            current_value = arr[index]
            right_eles = arr_cp[index+1:]
            if right_eles:
                max_value = max(right_eles)
                arr[index] = max_value
                if current_value == max_value:
                    arr_cp.remove(max_value)
            index += 1
        arr[-1] = -1
        return arr
