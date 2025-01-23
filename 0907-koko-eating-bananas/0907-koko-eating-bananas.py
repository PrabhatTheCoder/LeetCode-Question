class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = -1
        while low<=high:
            mid = low + (high-low)//2
            if self.EatingBananaInTime(piles,h,mid):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans

    def EatingBananaInTime(self, piles,h,speed):
        count = 0
        for i in range(len(piles)):
            if piles[i] <= speed:
                count += 1
            elif piles[i] % speed == 0:
                count += piles[i]//speed
            else:
                count += (piles[i]//speed) + 1  # V.IMP
        if count > h:
            return False
        else:
            return True

        