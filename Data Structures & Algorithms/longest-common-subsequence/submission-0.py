class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # two variable: i (text1), j (text2)
        # recurrence: i-1, j-1 || i, j-1 || i-1, j   i == j add 1
        # base case: i or j goes out of bounds

        memo = {}
        x, y = len(text1), len(text2)

        def dfs(i, j):
            if (i, j) in memo: return memo[(i, j)]

            if i not in range(x) or j not in range(y): return 0

            res = 0
            if text1[i] == text2[j]: 
                res = 1 + dfs(i-1, j-1)
            else:
                res = max(dfs(i, j-1), dfs(i-1, j))
            
            memo[(i, j)] = res
            return res
        return dfs(x - 1, y - 1)