class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res, subset = [], []
        
        def backtrack(target, start):

            if target == 0:
                res.append(subset[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > target:
                    continue

                subset.append(candidates[i])

                backtrack(target - candidates[i], i + 1)

                subset.pop()
        backtrack(target, 0)
        return res