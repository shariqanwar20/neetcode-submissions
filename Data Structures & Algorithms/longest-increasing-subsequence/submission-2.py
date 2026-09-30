class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # one parameter: index (max subsequence ending at index)
        # recurrence: find all comaptible smaller sequences and store the maxx one

        n = len(nums)
        if n == 1: return 1
        dp = [0] * (n + 1)
        res = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i + 1] = max(dp[i + 1], dp[j + 1])
            dp[i + 1] += 1
            res = max(res, dp[i + 1])
        return res