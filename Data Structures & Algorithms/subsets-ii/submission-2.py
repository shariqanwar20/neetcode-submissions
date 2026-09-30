class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        def backtrack(i, curr):
            

            res.append(curr.copy())
            prev = -21
            for j in range(i, len(nums)):
                if nums[j] == prev:
                    continue
                curr.append(nums[j])
                backtrack(j+1, curr)
                prev = nums[j]
                curr.pop()

        backtrack(0, [])
        return res

            
        