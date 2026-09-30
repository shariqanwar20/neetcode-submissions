class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # find duplicate with a set iterating over all number 
        
        ROWS, COLS = len(grid), len(grid[0])

        def find_repeated_value():
            num_set = set()
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] in num_set:
                        return grid[i][j]
                    num_set.add(grid[i][j])
        
        def find_missing_value(repeated_val):
            total_ideal = sum(range(1, ROWS ** 2 + 1))
            total_curr = 0
            for i in range(ROWS):
                for j in range(COLS):
                    total_curr += grid[i][j]

            total_curr -= repeated_val

            return total_ideal - total_curr

        repeated = find_repeated_value()
        return [repeated, find_missing_value(repeated)]



