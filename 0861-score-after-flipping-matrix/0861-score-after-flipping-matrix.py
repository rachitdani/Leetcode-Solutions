class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        #Flip all bits each row if the MSB (most significant bit) of that row is '0' (Greedy)
        for r in range(ROWS):
            if grid[r][0] == 0: 
                for c in range(COLS):
                    grid[r][c] = 1 if grid[r][c] == 0 else 0 # If '0', flip to '1' ; If '1', flip to '0' (flip the whole row)
        
        #Flip all bits each column & sum all binary numbers (represented by rows) simultaneously
        res = 0 
        for c in range(COLS):
            ones = 0 
            for r in range(ROWS):
                ones += grid[r][c]
            if ones < ROWS / 2: 
                res += (ROWS - ones) * 2**(COLS - c - 1) # We know '0's will be flipped to '1's eventually, so we accumulate `column's count of '0's` * `column's decimal value`
            else:
                res += ones * 2**(COLS - c - 1) # So just accumulate the result by adding `column's count of '1's` * `column's decimal value`
        return res 