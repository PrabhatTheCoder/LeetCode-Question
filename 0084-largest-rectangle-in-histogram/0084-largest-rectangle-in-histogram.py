class Solution:

    def NearestSmallestToLeft(self, arr: List[int]) -> int:
        # Initialize pseudo index for elements without a smaller left neighbor
        pseudo_idx = -1
        stack = []
        ans = []
        
        # Iterate through each element in the array
        for i in range(len(arr)):

            # If the stack is empty, no smaller element to the left
            if not stack:
                ans.append(pseudo_idx)

            # If the top of the stack is smaller, append its index
            elif stack and stack[-1][0] < arr[i]:
                ans.append(stack[-1][1])

            # If the top of the stack is greater or equal, pop until finding a smaller element
            elif stack and stack[-1][0] >= arr[i]:
                while stack and stack[-1][0] >= arr[i]:
                    stack.pop()

                # Append pseudo index if no smaller element is found
                if not stack:
                    ans.append(pseudo_idx)
                else:
                    ans.append(stack[-1][1])
            
            # Push current element and its index onto the stack
            stack.append((arr[i], i))

        return ans

    def NearestSmallestToRight(self, arr: List[int]) -> int:
        pseudo_idx = len(arr)
        stack = []
        ans = []
        
        for i in range(len(arr)-1, -1, -1):

            if not stack:
                ans.append(pseudo_idx)

            elif stack and stack[-1][0] < arr[i]:
                ans.append(stack[-1][1])

            elif stack and stack[-1][0] >= arr[i]:
                while stack and stack[-1][0] >= arr[i]:
                    stack.pop()

                if not stack:
                    ans.append(pseudo_idx)
                else:
                    ans.append(stack[-1][1])
            
            stack.append((arr[i], i))
        ans.reverse()
        return ans

                

    def largestRectangleArea(self, heights: List[int]) -> int:
        left = self.NearestSmallestToLeft(heights)
        right = self.NearestSmallestToRight(heights)

        width = []
        for i in range(len(left)):
            ans = right[i] - left[i] - 1 
            width.append(ans)

        area = []
        for i in range(len(width)):
            area.append(width[i] * heights[i])
        
        return max(area)
        