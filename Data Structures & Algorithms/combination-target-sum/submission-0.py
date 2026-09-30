class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, subset = [], []
        used = set()
        
        # goal = sum == target
        def backtrack(i):
            
            if i >= len(nums) or sum(subset) > target:
                return

            if sum(subset) == target:
                res.append(subset[::])
                return       

            subset.append(nums[i])
            backtrack(i)
            subset.pop()
            backtrack(i+1)

        backtrack(0)
        return res