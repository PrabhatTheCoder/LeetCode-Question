class Solution:
    # Function to find the minimum number of pages.
    def findPages(self, arr, k):
        # If the number of students is greater than the number of books, it's not possible
        if k > len(arr):
            return -1

        # Define search space
        low = max(arr)  # Minimum capacity: the largest book
        high = sum(arr)  # Maximum capacity: all books assigned to one student
        ans = -1

        # Binary search to find the minimum feasible capacity
        while low <= high:
            mid = low + (high - low) // 2
            if self.CheckCapacity(mid, arr, k):
                ans = mid  # Update answer
                high = mid - 1  # Try for a smaller maximum capacity
            else:
                low = mid + 1  # Increase the capacity

        return ans

    # Helper function to check if the capacity `mid` can accommodate `k` students
    def CheckCapacity(self, mid, arr, k):
        count = 1  # Start with one student
        current_pages = 0  # Pages assigned to the current student

        for pages in arr:
            # If adding this book exceeds the capacity, assign to a new student
            if current_pages + pages > mid:
                count += 1
                current_pages = pages  # Start new allocation
                if count > k:  # More students required than available
                    return False
            else:
                current_pages += pages

        return True



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends