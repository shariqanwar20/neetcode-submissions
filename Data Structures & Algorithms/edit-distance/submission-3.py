class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # base case: i and j both not in bounds i.e word is now equal

        memo = {}

        def dfs(i, j):
            if (i, j) in memo: return memo[(i, j)]
            # if i == 0 and j == 0: return 0

            res = math.inf
            # insert
            if i < 0:
                return j + 1
            # delete
            elif j < 0:
                return i + 1
            # replace, insert or delete
            else:
                if word1[i] == word2[j]:
                    res = min(res, dfs(i-1, j-1))
                else:
                    res = min(res, 1 + dfs(i, j - 1), 1 + dfs(i-1, j), 1 + dfs(i-1, j-1))
            memo[(i, j)] = res
            return res

        return dfs(len(word1) - 1, len(word2) - 1)


            