class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        memo = {}
        def dfs(balloons): 
            if tuple(balloons) in memo: return memo[tuple(balloons)]

            if not balloons: return 0

            res = 0
            for i in range(len(balloons)):
                coins = balloons[i]
                if i - 1 >= 0: coins *= balloons[i - 1]
                if i + 1 < len(balloons): coins *= balloons[i + 1]

                res = max(res, coins + dfs(balloons[:i] + balloons[i+1:]))
            
            memo[tuple(balloons)] = res
            return res

        dfs(nums)
        print(memo)
        return max(memo.values())
