class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters)-1

        # If target is greater than or equal to the last letter, wrap around to the first letter
        if target >= letters[high]:
            return letters[0]

        while low <= high:
            mid = low + (high - low) // 2

            if letters[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        # At the end of the loop, low will point to the smallest letter greater than target
        return letters[low]