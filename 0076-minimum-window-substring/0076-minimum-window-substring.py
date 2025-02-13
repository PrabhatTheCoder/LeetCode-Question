class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = float('inf')
        i = 0
        j = 0
        d = {}

        # Count characters in t
        for char in t:
            d[char] = d.get(char, 0) + 1
        
        count = len(d)  # Number of unique characters in t to be matched
        min_start = 0  # To store the start of the minimum window
        
        while j < len(s):
            # If the character at j is part of t, decrease its count in d
            if s[j] in d:
                d[s[j]] -= 1
                if d[s[j]] == 0:  # When the count reaches zero, one character is fully matched
                    count -= 1
            
            # If all characters are matched, try to minimize the window
            while count == 0:
                # Update the answer if the current window is smaller
                if (j - i + 1) < ans:
                    ans = j - i + 1
                    min_start = i
                
                # Move the left pointer to reduce the window size
                if s[i] in d:
                    d[s[i]] += 1
                    if d[s[i]] > 0:  # If a character's count goes above zero, it's no longer fully matched
                        count += 1
                        
                i += 1
            
            j += 1
        
        # Return the minimum window or empty string if no valid window is found
        return s[min_start:min_start + ans] if ans != float('inf') else ""
