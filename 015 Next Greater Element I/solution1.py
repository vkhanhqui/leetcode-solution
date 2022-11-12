from typing import List


class Solution:
    def nextGreaterElement(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[int]:
        result = []
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        index_1 = 0
        index_2 = 0
        is_eq = False
        while (
            index_1 < len_nums1
        ):
            if (
                not is_eq and
                nums1[index_1] == nums2[index_2]
            ):
                is_eq = True
            if (
                is_eq and
                nums2[index_2] > nums1[index_1]
            ):
                result.append(nums2[index_2])
                index_1 += 1
                index_2 = 0
                is_eq = False
                continue
            index_2 += 1
            if (
                index_2 > len_nums2 - 1
            ):
                result.append(-1)
                index_1 += 1
                index_2 = 0
                is_eq = False
        return result
