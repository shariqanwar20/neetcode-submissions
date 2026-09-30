class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # one variable remaining_amount

        memo = {}
        def dfs(target):
            if target in memo: return memo[target]

            if target < 0: return math.inf

            if target == 0: return 0

            res = math.inf
            for c in coins:
                res = min(res, dfs(target - c))

            memo[target] = res + 1
            return res + 1
        
        res = dfs(amount)
        return res if res != math.inf else -1