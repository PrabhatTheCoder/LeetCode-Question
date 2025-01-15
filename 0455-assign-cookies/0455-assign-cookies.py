class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        print(g)
        print(s)

        i = 0  # Pointer for children (g)
        j = 0  # Pointer for cookies (s)
        count = 0  # Content children count
        
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:  # If the current cookie satisfies the child
                count += 1
                i += 1  # Move to the next child
            j += 1  # Move to the next cookie regardless
        return count
        