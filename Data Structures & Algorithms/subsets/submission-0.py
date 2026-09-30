class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        
        # if goal reached; add to result
        def backtrack(start):
            res.append(subset[::])
        
            # iterate over all choices
            for i in range(start, len(nums)):
                    # make choice
                    subset.append(nums[i])
                    # backtrack
                    backtrack(i + 1)
                    # undo choice
                    subset.pop()
        
        backtrack(0)
        return res