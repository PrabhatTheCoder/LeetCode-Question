class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        val = 0
        for i in range(len(endTime)):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                val += 1

        return val 