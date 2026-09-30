class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res, subset = [], []
        used = set()
        
        def dfs():
            if len(subset) == len(nums):
                res.append(subset[::])
                return
            
            for j in range(len(nums)):
                if nums[j] not in used:
                    subset.append(nums[j])
                    used.add(nums[j])
                    dfs()
                    subset.pop()
                    used.remove(nums[j])

        dfs()
        return res
