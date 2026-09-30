class Solution:
    def rob(self, nums: List[int]) -> int:
        # one parameter: house number
        # recurrence: ith house + (i - 2) + (i + 2), (i-1) + (i+1)
        # base case: no houses left

        memo = {}

        def dfs(i):
            if i in memo: return memo[i]

            if i not in range(len(nums)): return 0

            max_amount = max(nums[i] + dfs(i + 2), dfs(i+1))
            memo[i] = max_amount

            return memo[i]
        
        return dfs(0)