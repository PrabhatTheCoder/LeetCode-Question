class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        

        for i in range(numRows):
            subArray = []
            for j in range(i+1):
                if i==j or j == 0:
                    subArray.append(1)
                else:
                    val = res[i-1][j-1] + res[i-1][j]
                    subArray.append(val)
            res.append(subArray)

        return res


        