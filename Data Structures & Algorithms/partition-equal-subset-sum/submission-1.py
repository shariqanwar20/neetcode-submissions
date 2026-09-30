class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # edge case: if not integer half return false
        if len(nums) == 1 or sum(nums) % 2: return False

        n = len(nums)
        # partition into equal => find a subset with sum of total / 2
        target = sum(nums) // 2
        # memo = {}
        # def knapsack(i, target):
        #     if (i, target) in memo: return memo[(i, target)]

        #     if i >= n or target < 0: return False

        #     if target == 0: return True

        #     memo[(i, target)] = knapsack(i+1, target) or knapsack(i+1, target - nums[i])
        #     return memo[(i, target)]

        # return knapsack(0, target)

        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i-1][j]
        return dp[n][target]
            

