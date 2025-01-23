class Solution:

    def check(self, time, mid, totalTrips):
        trips = 0
        for i in range(len(time)):
            trips += mid//time[i]
            if trips >= totalTrips:  # Early exit if we reach totalTrips
                return True
        return False


    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low = 1
        high = max(time) * totalTrips

        ans = -1
        while low<=high:

            mid = low + (high-low)//2
            if self.check(time,mid,totalTrips):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1

        return ans
        