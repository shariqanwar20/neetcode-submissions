class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        pacific, atlantic = set(), set()
                
        def traverse(r, c, visited):
            visited.add((r, c))
            for dr, dc in directions:
                next_i, next_j = r + dr, c + dc
                if next_i in range(ROWS) and next_j in range(COLS) and (next_i, next_j) not in visited and heights[next_i][next_j] >= heights[r][c]:
                    visited.add((next_i, next_j))
                    traverse(next_i, next_j, visited)
        
        for c in range(COLS):
            traverse(0, c, pacific)
            traverse(ROWS-1, c, atlantic)

        for r in range(ROWS):
            traverse(r, 0, pacific)
            traverse(r, COLS-1, atlantic)
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res