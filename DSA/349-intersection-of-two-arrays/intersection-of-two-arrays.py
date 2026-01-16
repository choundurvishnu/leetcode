class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums1)
        result=set()
        for i in s1:
            if i in nums2:
                result.add(i)
        return list(result)


        