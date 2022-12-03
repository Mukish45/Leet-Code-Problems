class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)

        i_12 = s1.intersection(s2)
        i_23 = s2.intersection(s3)
        i_13 = s1.intersection(s3)

        return list(i_12.union(i_23).union(i_13))