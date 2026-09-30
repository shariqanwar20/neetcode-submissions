class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # run bfs from every cell that is not -1 and INF if not visited
        # add 1 to the val

        # 3,  -1,  0,  1
        # 2, 2, 1,  -1 
        # 1, -1, 2,  -1
        # 0,   -1, 3,  4

        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def bfs(row, col):
            v = set()
            q = deque()
            q.append((row, col))

            while q:
                row, col = q.popleft()
                v.add((row, col))
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] != -1 and grid[r][c] != 0 and (r,c) not in v:
                        grid[r][c] = min(grid[r][c], grid[row][col] + 1)
                        q.append((r, c))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0 and (i, j) not in visit:
                    visit.add((i, j))
                    bfs(i, j)