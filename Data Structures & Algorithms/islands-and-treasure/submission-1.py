class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # run bfs from every cell that is not -1 and INF if not visited
        # add 1 to the val

        # 3,  -1,  0,  1
        # 2, 2, 1,  -1 
        # 1, -1, 2,  -1
        # 0,   -1, 3,  4

        
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def bfs(row, col):
            visit = set()
            q = deque()
            q.append((row, col))

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc

                    if new_r in range(ROWS) and new_c in range(COLS) and (new_r, new_c) not in visit and grid[new_r][new_c] > 0:
                        # unvisited land cell
                        grid[new_r][new_c] = min(grid[new_r][new_c], grid[r][c] + 1)
                        visit.add((new_r, new_c))
                        q.append((new_r, new_c))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    bfs(i, j)