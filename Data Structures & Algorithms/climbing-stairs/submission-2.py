class Solution:
    def climbStairs(self, n: int) -> int:
        # [_, _, _, _, n]

        # you are at the bottom.
        # one changing parameter. position p

        # (p+1)
        # (p+2)

        # base case: p == n (top of staircase)

        # memoized
        # memo = defaultdict(int)

        # def climb(pos):
        #     if memo[pos]: return memo[pos]

        #     if pos > n:
        #         memo[pos] = 0
        #         return 0

        #     if pos == n:
        #         memo[pos] += 1
        #         return 1
        #     val = climb(pos + 1) + climb(pos + 2)
        #     memo[pos] = val

        #     return memo[pos]
        # return climb(0)


        # bottom-up
        dp = [0 for _ in range(n+2)]
        dp[1], dp[2] = 1, 2
        
        for top in range(3, n+1):
            dp[top] = dp[top - 2] + dp[top - 1]
        return dp[n]

