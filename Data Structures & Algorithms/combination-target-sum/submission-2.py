class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.res = []
        def dfs(i, subset, curr_sum):
            if curr_sum > target:
                return
            if curr_sum == target:
                self.res.append(subset[::])
                return
            
            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j, subset, curr_sum + nums[j])
                subset.pop()

        dfs(0, [], 0)
        return self.res