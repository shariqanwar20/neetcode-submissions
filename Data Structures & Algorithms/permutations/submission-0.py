class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res, permutation = [], []

        used = set()
        def backtrack():
            
            if len(permutation) == len(nums):
                res.append(permutation[::])
                return
            
            for i in range(len(nums)):
                if nums[i] not in used:
                    permutation.append(nums[i])
                    used.add(nums[i])

                    backtrack()

                    permutation.pop()
                    used.remove(nums[i])
        backtrack()
        return res