class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # 1. iterate every cell in grid
        # 2. when a cell of value "1" is found, increase island number. Do DFS with IT
        # 3. continue till all cells are proceesed

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        # dfs functino on searching "1" and change to "0"
        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]=="0":
                return 

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c+dc)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] =="1":
                    dfs(r ,c)
                    islands +=1
        
        return islands

