class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # l= 0, r = 1
        # res = 1

        l = 0
        res = 0
        used = set()
        for r in range(len(s)):
            while l < r and s[r] in used:
                used.remove(s[l])
                l += 1

            used.add(s[r])
            res = max(res, r - l + 1)
        return res