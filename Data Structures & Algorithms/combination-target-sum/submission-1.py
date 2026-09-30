class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        # goal = sum == target
        def backtrack(candidates, target, start, currCombo, result):
            # If the current combination sums to target, add it to result
            if target == 0:
                result.append(list(currCombo))
                return
            
            for i in range(start, len(candidates)):
                # If the candidate is greater than the remaining target, skip it
                if candidates[i] > target:
                    continue
                
                # Make the choice to include candidates[i]
                currCombo.append(candidates[i])
                
                # Explore further with this choice (note that `i` is passed, not `i+1`, allowing reuse of the same element)
                backtrack(candidates, target - candidates[i], i, currCombo, result)
                
                # Undo the choice (backtrack)
                currCombo.pop()

        backtrack(nums, target, 0, [], res)
        return res