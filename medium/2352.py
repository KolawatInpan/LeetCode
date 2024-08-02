class Solution:
    def equalPairs(self, grid: list) -> int:
        row_hash = {}
        res = 0
        grid_transpose = []
        for i in range(len(grid[0])):
            grid_transpose.append([row[i] for row in grid])
        
        n = len(grid)
        for row in range(n):
            row_str = ','.join(map(str, grid[row]))
            if row_str not in row_hash:
                row_hash[row_str] = 1
            else:
                row_hash[row_str] += 1
        
        for col in range(n):
            col_str = ','.join(map(str, grid_transpose[col]))
            for j in range(row_hash.get(col_str, 0)):
                
                
        return res
        
print(Solution().equalPairs([[1, 1], [1, 1]]))  # 4