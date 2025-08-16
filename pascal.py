class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        t=[]
        for i in range(numRows):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=t[i-1][j-1]+t[i-1][j]
            t.append(row)
        return t
obj = Solution()
print(obj.generate(6))
