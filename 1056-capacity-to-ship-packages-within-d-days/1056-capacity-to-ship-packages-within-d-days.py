class Solution:
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lowCapacity = 0
        highCapacity = 0

        for i in range(len(weights)):
            if weights[i] >= lowCapacity:
                lowCapacity = weights[i]
            highCapacity += weights[i]

        minCapacityToShipPackage = -1
        while lowCapacity<=highCapacity:
            mid = lowCapacity + (highCapacity-lowCapacity)//2
            if self.CheckCapacity(mid,weights,days) == True:
                highCapacity = mid - 1
                minCapacityToShipPackage = mid
            else:
                lowCapacity = mid + 1
        return minCapacityToShipPackage

    def CheckCapacity(self, mid, weights, days):
        m = mid 
        count = 1
        for i in range(len(weights)):
            if m >= weights[i]:
                m -= weights[i]
            else:
                count += 1
                m = mid
                m -= weights[i]

        if count > days:
            return False
        else:
            return True


        