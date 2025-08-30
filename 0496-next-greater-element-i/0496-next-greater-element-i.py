class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = []
        stack = []
        nge_map = {}

        for j in range(len(nums2)-1, -1, -1):

            while stack and stack[-1] < nums2[j]:
                stack.pop()

            if not stack:
                nge_map[nums2[j]] = -1
                stack.append(nums2[j])

            elif nums2[j] < stack[-1]:
                nge_map[nums2[j]] = stack[-1]
                stack.append(nums2[j])
            
        for num in nums1:
            ans.append(nge_map[num])
        
        return ans

                



            


        