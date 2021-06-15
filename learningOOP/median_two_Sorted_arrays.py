class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x = []
        for i in nums1:
            x.append(float(i))
        for i in nums2:
            x.append(float(i))
        x = sorted(x)
        if len(x)% 2 == 0:
            med = int(len(x)/2)
            median = (x[med-1] + x[med]) /2
            return median
        else:
            med = len(x)/2
            median = int(med + 0.5)
            return x[median]



z = Solution()
k =z.findMedianSortedArrays(nums1=[1,2], nums2=[3,4])
print(k)