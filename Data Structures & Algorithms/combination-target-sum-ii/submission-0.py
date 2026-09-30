class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        def dfs(i, curr, target): 
            # stop if target met or exceeded
            if i > len(candidates):
                return

            if sum(curr) > target:
                return

            if sum(curr) == target:
                res.append(curr.copy())
                return

            # iterate over all availble numbers
            prev = -1
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                curr.append(candidates[j])
                dfs(j+1, curr, target)
                prev = candidates[j]
                curr.pop()

        dfs(0, [], target)
        return res
