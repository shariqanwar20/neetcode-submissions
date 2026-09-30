class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # condition: sliding window string should not have duplicates

        charset = set()
        res = 0

        l = 0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            
            res = max(res, r-l+1)
            charset.add(s[r])
        return res

