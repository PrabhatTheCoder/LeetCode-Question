class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        maxMD = 0

        north = 0
        west = 0
        east = 0
        south = 0

        for i in range(len(s)):
            
            if s[i] == 'E':
                east += 1

            elif s[i] == 'W':
                west += 1

            elif s[i] == 'N':
                north += 1

            elif s[i] == 'S':
                south += 1

            currMD = abs(east - west) + abs(north - south)
            steps = i + 1

            wasted = steps - currMD

            extra = 0
            if wasted != 0:
                extra = min(2 * k, wasted)

            finalCurrentMD = currMD + extra
            maxMD = max(finalCurrentMD, maxMD)

        return maxMD

            


