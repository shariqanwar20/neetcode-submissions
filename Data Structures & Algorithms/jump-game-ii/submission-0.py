class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo: return memo[i]

            if i >= len(nums): return math.inf

            if i == len(nums) - 1: return 0

            res = math.inf
            for j in range(1, nums[i] + 1):
                res = min(res, 1 + dfs(i + j))
            memo[i] = res
            return res
        return dfs(0)

