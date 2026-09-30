class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
                    visit.add((i, j))
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        time = -1

        while queue:
            time += 1
            n = len(queue)

            for i in range(n):
                row, col = queue.popleft()

                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and (r, c) not in visit and grid[r][c] == 1:
                        fresh -= 1
                        visit.add((r, c))
                        queue.append((r, c))

        return max(time, 0) if fresh == 0 else -1

