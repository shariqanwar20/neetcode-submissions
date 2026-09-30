class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [_, _, _, _, n] (n+1)
        # one variable: position

        # (pos + 1), (pos + 2)  min_cost  i.e mincost to reach floor pos
        # base case: n+1 th floor or above n+1

        n = len(cost)

        dp = [math.inf for _ in range(n + 1)]
        dp[n] = 0
        dp[n - 1] = cost[n - 1]

        for i in range(n-2, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        return min(dp[0], dp[1])


        memo = {}
        
        def climb(pos):
            if pos in memo: return memo[pos]

            if pos >= (n + 1): 
                return 0

            memo[pos] = cost[pos] + min(climb(pos + 1), climb(pos + 2))
            memo[pos] = val

            return val
        return min(climb(0), climb(1))
            