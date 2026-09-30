class Solution:
    def rob(self, nums: List[int]) -> int:
        # one parameter: house index

        # recurrence: ith house + dp(i+2), dp(i+1) check if i+2 or i+1 is not a neighbor

        # base case: no houses
        
        n = len(nums)
        if n == 1: return nums[0]

        def dfs(i, last, memo):
            if i in memo: return memo[i]

            if i > last: return 0
        
            max_amount = max(nums[i] + dfs(i + 2, last, memo), dfs(i+1, last, memo))
            memo[i] = max_amount
            return max_amount
        
        return max(dfs(0, n-2, {}), dfs(1, n-1, {}))
    

            