class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ans = []
        i = 0 
        j = 0 

        while i <= m - 1 and j <= n - 1:
            if nums1[i] <= nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1

        while i <= m - 1:
            ans.append(nums1[i])
            i += 1

        while j <= n - 1:
            ans.append(nums2[j])
            j += 1

        for k in range(m + n):
            nums1[k] = ans[k]
