class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row, col = len(grid) , len(grid[0])
        def f(i,j,sum):
            if i <0 or i>=row or j <0 or j>=col or grid[i][j]==0:
                return sum
            temp = grid[i][j]
            sum+=temp
            grid[i][j]=0
            ans = max(f(i+1,j,sum),f(i-1,j,sum),f(i,j+1,sum),f(i,j-1,sum))
            grid[i][j]=temp
            return ans
        gold = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]!=0:
                    gold = max(gold,f(i,j,0))
        return gold
            