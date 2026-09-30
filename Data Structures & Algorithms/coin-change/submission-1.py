class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # one variable remaining_amount

        # memo = {}
        # def dfs(target):
        #     if target in memo: return memo[target]

        #     if target < 0: return math.inf

        #     if target == 0: return 0

        #     res = math.inf
        #     for c in coins:
        #         res = min(res, dfs(target - c))

        #     memo[target] = res + 1
        #     return res + 1
        
        # res = dfs(amount)
        # return res if res != math.inf else -1

        dp = [math.inf for _ in range(amount + 1)]
        dp[0] = 0

        for target in range(1, amount + 1):
            res = math.inf
            for c in coins:
                if target - c >= 0:
                    res = min(res, 1 + dp[target - c])
            dp[target] = res

        print(dp)
        return dp[amount] if dp[amount] != math.inf else -1

