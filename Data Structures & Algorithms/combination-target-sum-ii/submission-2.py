class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        def dfs(i, subset, curr_sum):
            if curr_sum > target:
                return

            if curr_sum == target:
                res.append(subset[::])
                return
            
            # Lessons
            # 1. adding while inside for wont affect for's index
            # 2. dont add unneccessary checks at base case
            for j in range(i, len(candidates)):  # 1, 5
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                subset.append(candidates[j])
                dfs(j + 1, subset, curr_sum + candidates[j])
                subset.pop()


        dfs(0, [], 0)
        return res
            
        