class Solution:
    def jump(self, nums: List[int]) -> int:
        # memo = {}

        # def dfs(i):
        #     if i in memo: return memo[i]

        #     if i >= len(nums): return math.inf

        #     if i == len(nums) - 1: return 0

        #     res = math.inf
        #     for j in range(1, nums[i] + 1):
        #         res = min(res, 1 + dfs(i + j))
        #     memo[i] = res
        #     return res
        # return dfs(0)

        # [2, 3, 1, 1, 1, 1]
        dp = [math.inf for _ in range(len(nums))]
        # [0, 1, 1, 1, 1, 2]
        dp[0] = 0

        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j < len(dp):
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[len(nums) - 1]