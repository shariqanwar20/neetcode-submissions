class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Base case: word matches target

        # add word to subset if it matches position; backtrack in all directions if not used
        ROWS, COLS = len(board), len(board[0])
        visitSet = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(row, col, path):
            prefix = path + board[row][col]
            print("PREFIX: ", prefix)
            if len(prefix) > len(word):
                return False

            if len(prefix) == len(word):
                if prefix == word:
                    return True
                return False

            res = False
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r not in range(ROWS) or c not in range(COLS) or (r, c) in visitSet: continue
                
                visitSet.add((r, c))
                res = res or dfs(r, c, prefix)
                visitSet.remove((r, c))
            return res
        
        
        for i in range(ROWS):
            for j in range(COLS):
                visitSet.clear()
                visitSet.add((i, j))
                if dfs(i, j, ""):
                    return True
            
        return False
                    


            