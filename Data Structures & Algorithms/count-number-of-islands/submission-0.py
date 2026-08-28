class Solution:
    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        if grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.dfs(grid, i-1, j)#up
        self.dfs(grid, i, j-1)#left
        self.dfs(grid, i, j+1)#right
        self.dfs(grid, i+1, j)#down

    def numIslands(self, grid: List[List[str]]) -> int:
        islands_count = 0
        grid = [["0"] * len(grid[0])] + grid
        grid.append(["0"] * len(grid[0]))
        for i in range(len(grid)):
            grid[i] = ["0"] + grid[i] + ["0"]

        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == "1":
                    islands_count += 1
                    grid[i][j] = "0"
                    self.dfs(grid, i-1, j)#up
                    self.dfs(grid, i, j-1)#left
                    self.dfs(grid, i, j+1)#right
                    self.dfs(grid, i+1, j)#down
        return islands_count
