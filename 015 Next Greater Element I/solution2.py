from typing import List


class Solution:
    def nextGreaterElement(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[int]:
        nums1_indices = {
            number: index
            for index, number in enumerate(nums1)
        }
        result = [-1] * len(nums1)
        stack = []
        for index in range(len(nums2)):
            current_value_2 = nums2[index]
            while stack and current_value_2 > stack[-1]:
                number_1 = stack.pop()
                index_1 = nums1_indices[number_1]
                result[index_1] = current_value_2
            if current_value_2 in nums1_indices:
                stack.append(current_value_2)
        return result
