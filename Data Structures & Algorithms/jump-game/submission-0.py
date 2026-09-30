class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # one variable: pos

        memo = {}
        def dfs(i):
            if i in memo: return memo[i]

            if i >= len(nums): return False

            if i == len(nums) - 1: return True

            res = False
            for step in range(1, nums[i] + 1):
                res = res or dfs(i + step)
            memo[i] = res
            return res
        return dfs(0)