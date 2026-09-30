class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        map_r = defaultdict(set)
        map_c = defaultdict(set)
        map_box = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == ".":
                    continue
                r, c, box_r, box_c = i, j, i // 3, j // 3


                if (r in map_r[val] or c in map_c[val] or (box_r, box_c) in map_box[val]):
                    return False

                map_r[val].add(r)
                map_c[val].add(c)
                map_box[val].add((box_r, box_c))
        return True