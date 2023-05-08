"""
s30 - TC = O(M+N) and SC = O(1) where M = length of array nums1, 
N = length of array nums2
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr1 = len(nums1)-1-n
        ptr2 = len(nums2)-1
        ptr3 = len(nums1)-1
        while ptr1 >=0 and ptr2 >=0 and ptr3>=0:
            if nums1[ptr1] >= nums2[ptr2]:
                nums1[ptr3] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr3] = nums2[ptr2]
                ptr2 -= 1
            ptr3 -= 1
        while ptr2 >= 0:
            nums1[ptr3] = nums2[ptr2]
            ptr2 -= 1
            ptr3 -= 1
        while ptr1 >= 0:
            nums1[ptr3] = nums1[ptr1]
            ptr1 -= 1
            ptr3 -= 1