class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        sweep_line = [0]*n
        for i in range(len(bookings)):

            first = bookings[i][0]-1
            last = bookings[i][1]
            seats = bookings[i][2]

            sweep_line[first] += seats
            if last < n:
                sweep_line[last] -= seats

        prefixSum = [0]*n
        prefixSum[0] = sweep_line[0]
        for i in range(1,n):
            prefixSum[i] = prefixSum[i-1] + sweep_line[i]

        return prefixSum
        