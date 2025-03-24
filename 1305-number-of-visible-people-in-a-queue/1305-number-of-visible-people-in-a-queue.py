class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = []
        stack = []
        n = len(heights)-1
        for i in range(n,-1,-1):

            j = 0
            while stack and stack[-1] <= heights[i]:
                j += 1
                stack.pop()
            if not stack:
                ans.append(j)
            else:
                ans.append(j+1)

            stack.append(heights[i])
        ans.reverse()
        return ans
            
        
        