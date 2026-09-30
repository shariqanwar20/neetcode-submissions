class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # two variables: i (row), j (col)
        # recurrence: go down (i+1, j) + go right (i, j+1)
        # base case: out of bounds (0) || finish point (1)

        memo = {}

        def dfs(i, j):
            if (i, j) in memo: return memo[(i, j)]

            if i not in range(m) or j not in range(n): return 0

            if i == m-1 and j == n-1: return 1

            res = dfs(i + 1, j) + dfs(i, j + 1)
            memo[(i, j)] = res
            return res
            
        return dfs(0, 0)